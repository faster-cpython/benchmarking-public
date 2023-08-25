
# Results vs. 3.10.4

- fork: python
- ref: 3dd6ee2c0022cb49e5cb
- machine: windows-amd64
- commit hash: 3dd6ee2
- commit date: 2022-11-11
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.68 ms: 1.26x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.8 ms: 1.26x faster                                                       |
| tornado_http   | 109 ms                                                      | 92.6 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.8 ms: 1.19x faster                                                       |
| nbody          | 69.3 ms                                                     | 64.7 ms: 1.07x faster                                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.4 ms: 1.23x faster                                                       |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.19 ms: 1.64x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 189 us: 1.36x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 131 us: 1.30x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 88.9 ms: 1.14x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.65 us: 1.06x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                                       |
| pickle               | 6.80 us                                                     | 6.90 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.5 ms: 1.08x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.37 ms: 1.38x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.8 ms: 1.29x faster                                                       |
| django_template | 28.2 ms                                                     | 22.4 ms: 1.26x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 33.2 ms: 1.22x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.29 ms: 1.82x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.19 ms: 1.64x faster                                                       |
| mypy2                   | 352 ms                                                      | 221 ms: 1.59x faster                                                        |
| logging_silent          | 96.4 ns                                                     | 60.7 ns: 1.59x faster                                                       |
| go                      | 136 ms                                                      | 88.3 ms: 1.54x faster                                                       |
| richards                | 41.2 ms                                                     | 26.8 ms: 1.54x faster                                                       |
| scimark_sor             | 105 ms                                                      | 69.9 ms: 1.50x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 57.6 ms: 1.48x faster                                                       |
| raytrace                | 271 ms                                                      | 190 ms: 1.43x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.6 ms: 1.41x faster                                                       |
| pyflate                 | 387 ms                                                      | 280 ms: 1.38x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.37 ms: 1.38x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.4 ms: 1.37x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 189 us: 1.36x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 908 us: 1.34x faster                                                        |
| pycparser               | 868 ms                                                      | 653 ms: 1.33x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.15 ms: 1.33x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 804 ms: 1.33x faster                                                        |
| chaos                   | 58.9 ms                                                     | 45.1 ms: 1.31x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 131 us: 1.30x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 382 ms: 1.30x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.8 ms: 1.29x faster                                                       |
| thrift                  | 615 us                                                      | 486 us: 1.27x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.68 ms: 1.26x faster                                                       |
| html5lib                | 46.5 ms                                                     | 36.8 ms: 1.26x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 22.6 us: 1.26x faster                                                       |
| async_tree_none         | 420 ms                                                      | 334 ms: 1.26x faster                                                        |
| django_template         | 28.2 ms                                                     | 22.4 ms: 1.26x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 30.6 ns: 1.24x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 478 ms: 1.23x faster                                                        |
| regex_compile           | 103 ms                                                      | 84.4 ms: 1.23x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 63.6 ms: 1.23x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 985 ms: 1.23x faster                                                        |
| async_generators        | 224 ms                                                      | 183 ms: 1.22x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 33.2 ms: 1.22x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| float                   | 60.2 ms                                                     | 50.8 ms: 1.19x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 33.0 ms: 1.18x faster                                                       |
| tornado_http            | 109 ms                                                      | 92.6 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 517 ms: 1.18x faster                                                        |
| 2to3                    | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| dask                    | 305 ms                                                      | 261 ms: 1.17x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.2 ms: 1.15x faster                                                       |
| deepcopy                | 255 us                                                      | 223 us: 1.15x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| scimark_fft             | 193 ms                                                      | 169 ms: 1.15x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 88.9 ms: 1.14x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 178 ms: 1.14x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 689 us: 1.13x faster                                                        |
| json                    | 3.05 ms                                                     | 2.70 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.93 us: 1.12x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 852 us: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.40 ms: 1.11x faster                                                       |
| sympy_expand            | 315 ms                                                      | 286 ms: 1.10x faster                                                        |
| fannkuch                | 258 ms                                                      | 235 ms: 1.10x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.5 ms: 1.10x faster                                                       |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.58 sec: 1.09x faster                                                      |
| sympy_str               | 188 ms                                                      | 174 ms: 1.09x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 62.1 ms: 1.08x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.5 ms: 1.08x faster                                                       |
| nbody                   | 69.3 ms                                                     | 64.7 ms: 1.07x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.9 ms: 1.07x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.65 us: 1.06x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                                       |
| sympy_sum               | 104 ms                                                      | 98.8 ms: 1.05x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 73.8 ms: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.05x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 71.5 ms: 1.01x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.8 us: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.83 ms: 1.01x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.90 us: 1.01x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.85 us: 1.03x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.40 us: 1.03x slower                                                       |
| pidigits                | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| asyncio_tcp             | 712 ms                                                      | 765 ms: 1.07x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.4 us: 1.14x slower                                                       |
| generators              | 31.6 ms                                                     | 37.3 ms: 1.18x slower                                                       |
| coverage                | 40.0 ms                                                     | 55.5 ms: 1.39x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                                |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
