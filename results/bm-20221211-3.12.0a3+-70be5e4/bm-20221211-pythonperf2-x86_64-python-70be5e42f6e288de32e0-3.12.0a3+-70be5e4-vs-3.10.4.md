
# Results vs. 3.10.4

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: linux-x86_64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.48 ms: 1.30x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.3 ms: 1.54x faster                                                        |
| float          | 110 ms                                                       | 73.3 ms: 1.50x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.7 ms: 1.12x faster                                                        |
| regex_dna      | 259 ms                                                       | 236 ms: 1.10x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 216 us: 1.48x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 311 us: 1.47x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 54.3 ms: 1.40x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 79.5 ms: 1.19x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.70 us: 1.11x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.0 us: 1.09x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.33 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.04x faster                                                         |
| pickle               | 9.94 us                                                      | 9.71 us: 1.02x faster                                                        |
| pickle_dict          | 30.0 us                                                      | 31.6 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 53.1 ms: 1.22x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.73 ms: 2.00x faster                                                        |
| scimark_sor             | 177 ms                                                       | 106 ms: 1.67x faster                                                         |
| logging_silent          | 166 ns                                                       | 99.3 ns: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.62x faster                                                        |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.62x faster                                                         |
| pyflate                 | 697 ms                                                       | 437 ms: 1.60x faster                                                         |
| richards                | 74.1 ms                                                      | 47.0 ms: 1.58x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.63 ms: 1.55x faster                                                        |
| go                      | 259 ms                                                       | 167 ms: 1.55x faster                                                         |
| nbody                   | 137 ms                                                       | 89.3 ms: 1.54x faster                                                        |
| raytrace                | 488 ms                                                       | 320 ms: 1.53x faster                                                         |
| float                   | 110 ms                                                       | 73.3 ms: 1.50x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 216 us: 1.48x faster                                                         |
| sqlglot_parse           | 2.26 ms                                                      | 1.53 ms: 1.47x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 311 us: 1.47x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.89 ms: 1.44x faster                                                        |
| spectral_norm           | 136 ms                                                       | 95.6 ms: 1.42x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 84.0 ms: 1.41x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 54.3 ms: 1.40x faster                                                        |
| html5lib                | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.74 ms: 1.39x faster                                                        |
| chaos                   | 107 ms                                                       | 77.2 ms: 1.39x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.94 ms: 1.37x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 771 ms: 1.36x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 36.2 us: 1.35x faster                                                        |
| async_tree_none         | 700 ms                                                       | 520 ms: 1.34x faster                                                         |
| async_tree_memoization  | 824 ms                                                       | 618 ms: 1.33x faster                                                         |
| django_template         | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 45.7 ns: 1.30x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.48 ms: 1.30x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.87 us: 1.30x faster                                                        |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                         |
| regex_compile           | 194 ms                                                       | 150 ms: 1.29x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| async_generators        | 422 ms                                                       | 328 ms: 1.29x faster                                                         |
| thrift                  | 1.16 ms                                                      | 905 us: 1.29x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.28x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.59 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 760 ms: 1.25x faster                                                         |
| mypy2                   | 466 ms                                                       | 373 ms: 1.25x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.0 us: 1.25x faster                                                        |
| 2to3                    | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| fannkuch                | 496 ms                                                       | 405 ms: 1.22x faster                                                         |
| genshi_xml              | 64.7 ms                                                      | 53.1 ms: 1.22x faster                                                        |
| deepcopy                | 454 us                                                       | 373 us: 1.22x faster                                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.33 us: 1.21x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.1 ms: 1.21x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 66.7 ms: 1.20x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                         |
| xml_etree_generate      | 94.6 ms                                                      | 79.5 ms: 1.19x faster                                                        |
| json                    | 5.96 ms                                                      | 5.04 ms: 1.18x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 963 us: 1.18x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 18.8 ms: 1.16x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.58 ms: 1.15x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| nqueens                 | 112 ms                                                       | 98.2 ms: 1.15x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.65 sec: 1.15x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.61 us: 1.14x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 23.7 ms: 1.12x faster                                                        |
| dask                    | 463 ms                                                       | 413 ms: 1.12x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.70 us: 1.11x faster                                                        |
| sympy_expand            | 599 ms                                                       | 541 ms: 1.11x faster                                                         |
| asyncio_tcp             | 782 ms                                                       | 709 ms: 1.10x faster                                                         |
| regex_dna               | 259 ms                                                       | 236 ms: 1.10x faster                                                         |
| coroutines              | 30.4 ms                                                      | 27.7 ms: 1.10x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.0 us: 1.09x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.7 ms: 1.09x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.56 ms: 1.09x faster                                                        |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                         |
| unpickle_list           | 4.49 us                                                      | 4.33 us: 1.04x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 107 ms: 1.04x faster                                                         |
| pickle                  | 9.94 us                                                      | 9.71 us: 1.02x faster                                                        |
| sympy_sum               | 193 ms                                                       | 189 ms: 1.02x faster                                                         |
| comprehensions          | 26.9 us                                                      | 26.8 us: 1.01x faster                                                        |
| pickle_dict             | 30.0 us                                                      | 31.6 us: 1.05x slower                                                        |
| generators              | 58.0 ms                                                      | 61.2 ms: 1.05x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.75 ms: 1.09x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.14x slower                                                        |
| coverage                | 64.0 ms                                                      | 86.1 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x
