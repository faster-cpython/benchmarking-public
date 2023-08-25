
# Results vs. 3.10.4

- fork: python
- ref: e47b13934b2eb50914e4
- machine: windows-amd64
- commit hash: e47b139
- commit date: 2023-01-08
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.58 ms: 1.29x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.5 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.3 ms: 1.25x faster                                                       |
| nbody          | 69.3 ms                                                     | 60.2 ms: 1.15x faster                                                       |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 80.3 ms: 1.29x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.13 ms: 1.66x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 169 us: 1.52x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 122 us: 1.40x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.0 ms: 1.28x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 87.9 ms: 1.16x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.33 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.2 ms: 1.06x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.69 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.1 ms: 1.02x faster                                                       |
| pickle               | 6.80 us                                                     | 6.98 us: 1.03x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.77 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 13.4 ms: 1.43x faster                                                       |
| mako            | 8.80 ms                                                     | 6.23 ms: 1.41x faster                                                       |
| django_template | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.6 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.01 ms: 2.08x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 54.7 ns: 1.76x faster                                                       |
| richards                | 41.2 ms                                                     | 24.2 ms: 1.70x faster                                                       |
| scimark_sor             | 105 ms                                                      | 63.1 ms: 1.66x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.13 ms: 1.66x faster                                                       |
| go                      | 136 ms                                                      | 82.4 ms: 1.65x faster                                                       |
| mypy2                   | 352 ms                                                      | 218 ms: 1.61x faster                                                        |
| raytrace                | 271 ms                                                      | 176 ms: 1.54x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 169 us: 1.52x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 58.1 ms: 1.47x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 38.0 ms: 1.47x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 25.9 ns: 1.46x faster                                                       |
| pyflate                 | 387 ms                                                      | 267 ms: 1.45x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 3.82 ms: 1.45x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 498 ms: 1.43x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 20.0 us: 1.43x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.4 ms: 1.43x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 860 us: 1.42x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.23 ms: 1.41x faster                                                       |
| chaos                   | 58.9 ms                                                     | 41.8 ms: 1.41x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 122 us: 1.40x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 761 ms: 1.40x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                                       |
| async_tree_none         | 420 ms                                                      | 305 ms: 1.38x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 57.5 ms: 1.36x faster                                                       |
| thrift                  | 615 us                                                      | 454 us: 1.36x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 367 ms: 1.35x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 46.1 ms: 1.35x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                                       |
| pycparser               | 868 ms                                                      | 651 ms: 1.33x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 30.6 ms: 1.33x faster                                                       |
| html5lib                | 46.5 ms                                                     | 35.5 ms: 1.31x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.58 ms: 1.29x faster                                                       |
| regex_compile           | 103 ms                                                      | 80.3 ms: 1.29x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 940 ms: 1.28x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.0 ms: 1.28x faster                                                       |
| async_generators        | 224 ms                                                      | 175 ms: 1.28x faster                                                        |
| float                   | 60.2 ms                                                     | 48.3 ms: 1.25x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 475 ms: 1.24x faster                                                        |
| deepcopy                | 255 us                                                      | 207 us: 1.23x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 497 ms: 1.23x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 31.9 ms: 1.22x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.22 ms: 1.20x faster                                                       |
| 2to3                    | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| dask                    | 305 ms                                                      | 259 ms: 1.18x faster                                                        |
| fannkuch                | 258 ms                                                      | 219 ms: 1.17x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 57.1 ms: 1.17x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 87.9 ms: 1.16x faster                                                       |
| sympy_expand            | 315 ms                                                      | 272 ms: 1.16x faster                                                        |
| nbody                   | 69.3 ms                                                     | 60.2 ms: 1.15x faster                                                       |
| scimark_fft             | 193 ms                                                      | 168 ms: 1.15x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.88 us: 1.15x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 177 ms: 1.14x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 692 us: 1.13x faster                                                        |
| regex_dna               | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.3 ms: 1.11x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| json                    | 3.05 ms                                                     | 2.76 ms: 1.11x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 857 us: 1.10x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.33 us: 1.10x faster                                                       |
| comprehensions          | 16.0 us                                                     | 14.5 us: 1.10x faster                                                       |
| sympy_str               | 188 ms                                                      | 171 ms: 1.10x faster                                                        |
| sympy_sum               | 104 ms                                                      | 95.2 ms: 1.09x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.60 sec: 1.07x faster                                                      |
| xml_etree_generate      | 54.5 ms                                                     | 51.2 ms: 1.06x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.35 us: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.05x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.69 us: 1.05x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.5 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.0 ms: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.1 ms: 1.02x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.10 us: 1.02x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.77 ms: 1.00x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.98 us: 1.03x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 62.9 ms: 1.04x slower                                                       |
| generators              | 31.6 ms                                                     | 33.1 ms: 1.05x slower                                                       |
| pidigits                | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.77 us: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.2 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.22x faster                                                                |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x
