
# Results vs. 3.10.4

- fork: python
- ref: a1f08f5f19753c7c9295
- machine: windows-amd64
- commit hash: a1f08f5
- commit date: 2023-02-13
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.43 ms: 1.34x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.9 ms: 1.33x faster                                                       |
| tornado_http   | 109 ms                                                      | 90.3 ms: 1.21x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 49.6 ms: 1.21x faster                                                       |
| nbody          | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.6 ms: 1.32x faster                                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.4 ms: 1.04x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.27 ms: 1.61x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 169 us: 1.52x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 119 us: 1.44x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.06 us: 1.14x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.71 us: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 6.93 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.5 ms: 1.03x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.73 us: 1.05x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.3 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 5.99 ms: 1.47x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.5 ms: 1.41x faster                                                       |
| django_template | 28.2 ms                                                     | 21.0 ms: 1.35x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.39x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.96 ms: 2.13x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 54.7 ns: 1.76x faster                                                       |
| richards                | 41.2 ms                                                     | 23.9 ms: 1.72x faster                                                       |
| go                      | 136 ms                                                      | 82.0 ms: 1.66x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.27 ms: 1.61x faster                                                       |
| scimark_sor             | 105 ms                                                      | 66.1 ms: 1.59x faster                                                       |
| raytrace                | 271 ms                                                      | 174 ms: 1.56x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 169 us: 1.52x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 56.4 ms: 1.52x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 25.6 ns: 1.48x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.73 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 485 ms: 1.47x faster                                                        |
| mako                    | 8.80 ms                                                     | 5.99 ms: 1.47x faster                                                       |
| pyflate                 | 387 ms                                                      | 265 ms: 1.46x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 119 us: 1.44x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 43.9 ms: 1.42x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.4 ms: 1.42x faster                                                       |
| chaos                   | 58.9 ms                                                     | 41.6 ms: 1.42x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.5 ms: 1.41x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 867 us: 1.41x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 769 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.07 ms: 1.37x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 20.9 us: 1.37x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.0 ms: 1.35x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 370 ms: 1.34x faster                                                        |
| async_tree_none         | 420 ms                                                      | 314 ms: 1.34x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.43 ms: 1.34x faster                                                       |
| comprehensions          | 16.0 us                                                     | 12.0 us: 1.33x faster                                                       |
| html5lib                | 46.5 ms                                                     | 34.9 ms: 1.33x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| regex_compile           | 103 ms                                                      | 78.6 ms: 1.32x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 925 ms: 1.30x faster                                                        |
| pycparser               | 868 ms                                                      | 666 ms: 1.30x faster                                                        |
| thrift                  | 615 us                                                      | 480 us: 1.28x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 463 ms: 1.27x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 62.0 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 488 ms: 1.25x faster                                                        |
| deepcopy                | 255 us                                                      | 205 us: 1.25x faster                                                        |
| float                   | 60.2 ms                                                     | 49.6 ms: 1.21x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                                       |
| tornado_http            | 109 ms                                                      | 90.3 ms: 1.21x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 32.3 ms: 1.21x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| nqueens                 | 67.0 ms                                                     | 56.2 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.24 ms: 1.19x faster                                                       |
| 2to3                    | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 12.6 ms: 1.18x faster                                                       |
| sympy_expand            | 315 ms                                                      | 270 ms: 1.17x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.85 us: 1.17x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 176 ms: 1.15x faster                                                        |
| scimark_fft             | 193 ms                                                      | 168 ms: 1.15x faster                                                        |
| sympy_str               | 188 ms                                                      | 165 ms: 1.14x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.8 ms: 1.14x faster                                                       |
| fannkuch                | 258 ms                                                      | 226 ms: 1.14x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.06 us: 1.14x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 693 us: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 843 us: 1.12x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                                       |
| sympy_sum               | 104 ms                                                      | 93.3 ms: 1.12x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| nbody                   | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| json                    | 3.05 ms                                                     | 2.78 ms: 1.10x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.58 sec: 1.08x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                       |
| regex_dna               | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| logging_format          | 6.66 us                                                     | 6.31 us: 1.06x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.4 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.3 ms: 1.04x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.71 us: 1.04x faster                                                       |
| async_generators        | 224 ms                                                      | 216 ms: 1.04x faster                                                        |
| sqlite_synth            | 1.84 us                                                     | 1.79 us: 1.03x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.04 us: 1.03x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.9 ms: 1.02x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.82 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.93 us: 1.02x slower                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 65.5 ms: 1.03x slower                                                       |
| pidigits                | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.73 us: 1.05x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 64.0 ms: 1.05x slower                                                       |
| generators              | 31.6 ms                                                     | 33.7 ms: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.3 us: 1.14x slower                                                       |
| coverage                | 40.0 ms                                                     | 52.7 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.22x faster                                                                |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x
