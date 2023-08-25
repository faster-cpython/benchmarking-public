
# Results vs. 3.10.4

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: linux-x86_64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.60 ms: 1.28x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                        |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.1 ms: 1.54x faster                                                        |
| float          | 110 ms                                                       | 72.6 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| regex_dna      | 259 ms                                                       | 226 ms: 1.15x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 210 us: 1.53x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 304 us: 1.50x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 54.8 ms: 1.39x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 79.0 ms: 1.20x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| unpickle_list        | 4.49 us                                                      | 4.53 us: 1.01x slower                                                        |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 32.2 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.18 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 40.0 ms: 1.29x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 25.5 ms: 1.23x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 56.5 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.58 ms: 2.09x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 393 ms: 1.99x faster                                                         |
| logging_silent          | 166 ns                                                       | 99.5 ns: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 65.8 ms: 1.66x faster                                                        |
| raytrace                | 488 ms                                                       | 300 ms: 1.63x faster                                                         |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                         |
| go                      | 259 ms                                                       | 160 ms: 1.62x faster                                                         |
| richards                | 74.1 ms                                                      | 46.0 ms: 1.61x faster                                                        |
| pyflate                 | 697 ms                                                       | 436 ms: 1.60x faster                                                         |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.59x faster                                                         |
| nbody                   | 137 ms                                                       | 89.1 ms: 1.54x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 210 us: 1.53x faster                                                         |
| float                   | 110 ms                                                       | 72.6 ms: 1.52x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 304 us: 1.50x faster                                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.79 ms: 1.50x faster                                                        |
| chaos                   | 107 ms                                                       | 72.1 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.69 ms: 1.42x faster                                                        |
| html5lib                | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.66 ms: 1.42x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.59 ms: 1.42x faster                                                        |
| spectral_norm           | 136 ms                                                       | 96.9 ms: 1.41x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 84.3 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 54.8 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.96 ms: 1.38x faster                                                        |
| async_tree_none         | 700 ms                                                       | 510 ms: 1.37x faster                                                         |
| pprint_safe_repr        | 1.05 sec                                                     | 774 ms: 1.36x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 609 ms: 1.35x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 44.7 ns: 1.33x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 37.1 us: 1.32x faster                                                        |
| aiohttp                 | 1.21 ms                                                      | 927 us: 1.30x faster                                                         |
| django_template         | 51.5 ms                                                      | 40.0 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 741 ms: 1.28x faster                                                         |
| gunicorn                | 1.17 ms                                                      | 914 us: 1.28x faster                                                         |
| regex_compile           | 194 ms                                                       | 151 ms: 1.28x faster                                                         |
| chameleon               | 9.72 ms                                                      | 7.60 ms: 1.28x faster                                                        |
| thrift                  | 1.16 ms                                                      | 916 us: 1.27x faster                                                         |
| tornado_http            | 152 ms                                                       | 120 ms: 1.27x faster                                                         |
| async_generators        | 422 ms                                                       | 333 ms: 1.27x faster                                                         |
| scimark_fft             | 359 ms                                                       | 287 ms: 1.25x faster                                                         |
| logging_simple          | 8.90 us                                                      | 7.12 us: 1.25x faster                                                        |
| fannkuch                | 496 ms                                                       | 401 ms: 1.24x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 25.5 ms: 1.23x faster                                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                                         |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                       |
| 2to3                    | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| logging_format          | 9.57 us                                                      | 7.90 us: 1.21x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.5 ms: 1.20x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 66.9 ms: 1.20x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 79.0 ms: 1.20x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                                         |
| sqlglot_normalize       | 144 ms                                                       | 122 ms: 1.19x faster                                                         |
| nqueens                 | 112 ms                                                       | 95.8 ms: 1.17x faster                                                        |
| json                    | 5.96 ms                                                      | 5.09 ms: 1.17x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.45 us: 1.17x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.57 us: 1.15x faster                                                        |
| regex_dna               | 259 ms                                                       | 226 ms: 1.15x faster                                                         |
| genshi_xml              | 64.7 ms                                                      | 56.5 ms: 1.15x faster                                                        |
| deepcopy                | 454 us                                                       | 397 us: 1.14x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.59 ms: 1.14x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                        |
| sympy_expand            | 599 ms                                                       | 536 ms: 1.12x faster                                                         |
| dask                    | 463 ms                                                       | 415 ms: 1.12x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.10x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.77 sec: 1.09x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| coroutines              | 30.4 ms                                                      | 28.3 ms: 1.07x faster                                                        |
| sympy_str               | 358 ms                                                       | 333 ms: 1.07x faster                                                         |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                         |
| telco                   | 7.14 ms                                                      | 6.77 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| unpickle_list           | 4.49 us                                                      | 4.53 us: 1.01x slower                                                        |
| pickle                  | 9.94 us                                                      | 10.0 us: 1.01x slower                                                        |
| comprehensions          | 26.9 us                                                      | 27.3 us: 1.01x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.52 ms: 1.02x slower                                                        |
| generators              | 58.0 ms                                                      | 60.7 ms: 1.05x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 32.2 us: 1.07x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.18 ms: 1.12x slower                                                        |
| coverage                | 64.0 ms                                                      | 86.4 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
