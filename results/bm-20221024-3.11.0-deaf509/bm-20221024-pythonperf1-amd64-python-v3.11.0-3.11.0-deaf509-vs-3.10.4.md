
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: windows-amd64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.11x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 209 ms: 1.10x faster                                        |
| chameleon      | 5.77 ms                                                                  | 5.11 ms: 1.13x faster                                       |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                      |
| html5lib       | 47.3 ms                                                                  | 37.5 ms: 1.26x faster                                       |
| tornado_http   | 106 ms                                                                   | 91.8 ms: 1.16x faster                                       |
| Geometric mean | (ref)                                                                    | 1.16x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 54.6 ms: 1.09x faster                                       |
| nbody          | 71.5 ms                                                                  | 70.0 ms: 1.02x faster                                       |
| pidigits       | 145 ms                                                                   | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 90.6 ms: 1.14x faster                                       |
| regex_dna      | 131 ms                                                                   | 115 ms: 1.13x faster                                        |
| regex_effbot   | 1.64 ms                                                                  | 1.50 ms: 1.10x faster                                       |
| regex_v8       | 15.1 ms                                                                  | 13.8 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                                    | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 264 us                                                                   | 200 us: 1.32x faster                                        |
| json_dumps           | 9.00 ms                                                                  | 7.56 ms: 1.19x faster                                       |
| unpickle_pure_python | 179 us                                                                   | 152 us: 1.18x faster                                        |
| xml_etree_process    | 43.0 ms                                                                  | 37.1 ms: 1.16x faster                                       |
| json_loads           | 14.2 us                                                                  | 12.9 us: 1.10x faster                                       |
| unpickle             | 8.88 us                                                                  | 8.09 us: 1.10x faster                                       |
| unpickle_list        | 2.71 us                                                                  | 2.55 us: 1.07x faster                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 52.2 ms: 1.03x faster                                       |
| pickle_list          | 2.57 us                                                                  | 2.68 us: 1.04x slower                                       |
| pickle_dict          | 16.7 us                                                                  | 18.5 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                                    | 1.07x faster                                                |

Benchmark hidden because not significant (3): pickle, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.7 ms: 1.03x faster                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                                    | 1.02x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 24.1 ms: 1.21x faster                                       |
| mako            | 8.69 ms                                                                  | 7.26 ms: 1.20x faster                                       |
| genshi_text     | 18.5 ms                                                                  | 17.0 ms: 1.09x faster                                       |
| genshi_xml      | 38.8 ms                                                                  | 37.3 ms: 1.04x faster                                       |
| Geometric mean  | (ref)                                                                    | 1.13x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.61 ms: 1.59x faster                                       |
| mypy2                   | 337 ms                                                                   | 229 ms: 1.47x faster                                        |
| go                      | 143 ms                                                                   | 97.3 ms: 1.47x faster                                       |
| scimark_sor             | 104 ms                                                                   | 75.6 ms: 1.37x faster                                       |
| logging_silent          | 94.6 ns                                                                  | 69.8 ns: 1.35x faster                                       |
| richards                | 41.0 ms                                                                  | 30.6 ms: 1.34x faster                                       |
| pickle_pure_python      | 264 us                                                                   | 200 us: 1.32x faster                                        |
| scimark_lu              | 83.9 ms                                                                  | 63.5 ms: 1.32x faster                                       |
| async_tree_io           | 1.02 sec                                                                 | 779 ms: 1.31x faster                                        |
| async_tree_memoization  | 485 ms                                                                   | 371 ms: 1.31x faster                                        |
| async_tree_none         | 414 ms                                                                   | 320 ms: 1.29x faster                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 47.6 ms: 1.29x faster                                       |
| thrift                  | 632 us                                                                   | 491 us: 1.29x faster                                        |
| sqlglot_parse           | 1.22 ms                                                                  | 952 us: 1.28x faster                                        |
| pyflate                 | 388 ms                                                                   | 304 ms: 1.28x faster                                        |
| raytrace                | 267 ms                                                                   | 211 ms: 1.27x faster                                        |
| pycparser               | 873 ms                                                                   | 691 ms: 1.26x faster                                        |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.16 ms: 1.26x faster                                       |
| html5lib                | 47.3 ms                                                                  | 37.5 ms: 1.26x faster                                       |
| scimark_monte_carlo     | 56.0 ms                                                                  | 44.6 ms: 1.26x faster                                       |
| chaos                   | 58.4 ms                                                                  | 47.1 ms: 1.24x faster                                       |
| django_template         | 29.2 ms                                                                  | 24.1 ms: 1.21x faster                                       |
| async_generators        | 214 ms                                                                   | 178 ms: 1.21x faster                                        |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 501 ms: 1.21x faster                                        |
| hexiom                  | 5.45 ms                                                                  | 4.55 ms: 1.20x faster                                       |
| mako                    | 8.69 ms                                                                  | 7.26 ms: 1.20x faster                                       |
| json_dumps              | 9.00 ms                                                                  | 7.56 ms: 1.19x faster                                       |
| sqlalchemy_declarative  | 96.4 ms                                                                  | 81.5 ms: 1.18x faster                                       |
| unpickle_pure_python    | 179 us                                                                   | 152 us: 1.18x faster                                        |
| pprint_pformat          | 1.23 sec                                                                 | 1.04 sec: 1.18x faster                                      |
| dask                    | 310 ms                                                                   | 264 ms: 1.17x faster                                        |
| xml_etree_process       | 43.0 ms                                                                  | 37.1 ms: 1.16x faster                                       |
| pprint_safe_repr        | 593 ms                                                                   | 512 ms: 1.16x faster                                        |
| tornado_http            | 106 ms                                                                   | 91.8 ms: 1.16x faster                                       |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                      |
| regex_compile           | 103 ms                                                                   | 90.6 ms: 1.14x faster                                       |
| regex_dna               | 131 ms                                                                   | 115 ms: 1.13x faster                                        |
| chameleon               | 5.77 ms                                                                  | 5.11 ms: 1.13x faster                                       |
| deepcopy_memo           | 28.4 us                                                                  | 25.2 us: 1.13x faster                                       |
| bench_thread_pool       | 953 us                                                                   | 852 us: 1.12x faster                                        |
| sqlglot_optimize        | 38.7 ms                                                                  | 34.9 ms: 1.11x faster                                       |
| sqlalchemy_imperative   | 11.3 ms                                                                  | 10.2 ms: 1.11x faster                                       |
| create_gc_cycles        | 764 us                                                                   | 693 us: 1.10x faster                                        |
| json_loads              | 14.2 us                                                                  | 12.9 us: 1.10x faster                                       |
| unpickle                | 8.88 us                                                                  | 8.09 us: 1.10x faster                                       |
| 2to3                    | 229 ms                                                                   | 209 ms: 1.10x faster                                        |
| regex_effbot            | 1.64 ms                                                                  | 1.50 ms: 1.10x faster                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.68 us: 1.10x faster                                       |
| genshi_text             | 18.5 ms                                                                  | 17.0 ms: 1.09x faster                                       |
| spectral_norm           | 74.3 ms                                                                  | 67.9 ms: 1.09x faster                                       |
| regex_v8                | 15.1 ms                                                                  | 13.8 ms: 1.09x faster                                       |
| float                   | 59.5 ms                                                                  | 54.6 ms: 1.09x faster                                       |
| aiohttp                 | 968 us                                                                   | 899 us: 1.08x faster                                        |
| coroutines              | 15.6 ms                                                                  | 14.6 ms: 1.07x faster                                       |
| unpickle_list           | 2.71 us                                                                  | 2.55 us: 1.07x faster                                       |
| sympy_integrate         | 14.7 ms                                                                  | 13.8 ms: 1.06x faster                                       |
| sympy_expand            | 313 ms                                                                   | 295 ms: 1.06x faster                                        |
| sqlglot_normalize       | 201 ms                                                                   | 190 ms: 1.06x faster                                        |
| dulwich_log             | 47.0 ms                                                                  | 44.5 ms: 1.06x faster                                       |
| pathlib                 | 75.2 ms                                                                  | 71.4 ms: 1.05x faster                                       |
| deepcopy_reduce         | 2.18 us                                                                  | 2.07 us: 1.05x faster                                       |
| scimark_fft             | 187 ms                                                                   | 178 ms: 1.05x faster                                        |
| deepcopy                | 256 us                                                                   | 246 us: 1.04x faster                                        |
| genshi_xml              | 38.8 ms                                                                  | 37.3 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.57 ms: 1.04x faster                                       |
| sympy_str               | 189 ms                                                                   | 182 ms: 1.04x faster                                        |
| pylint                  | 337 ms                                                                   | 326 ms: 1.03x faster                                        |
| xml_etree_generate      | 53.8 ms                                                                  | 52.2 ms: 1.03x faster                                       |
| python_startup          | 19.3 ms                                                                  | 18.7 ms: 1.03x faster                                       |
| sympy_sum               | 102 ms                                                                   | 99.9 ms: 1.02x faster                                       |
| nbody                   | 71.5 ms                                                                  | 70.0 ms: 1.02x faster                                       |
| flaskblogging           | 2.05 sec                                                                 | 2.04 sec: 1.00x faster                                      |
| meteor_contest          | 74.3 ms                                                                  | 74.7 ms: 1.01x slower                                       |
| pidigits                | 145 ms                                                                   | 148 ms: 1.02x slower                                        |
| telco                   | 3.77 ms                                                                  | 3.90 ms: 1.04x slower                                       |
| mdp                     | 1.60 sec                                                                 | 1.67 sec: 1.04x slower                                      |
| pickle_list             | 2.57 us                                                                  | 2.68 us: 1.04x slower                                       |
| asyncio_tcp             | 664 ms                                                                   | 699 ms: 1.05x slower                                        |
| bench_mp_pool           | 59.2 ms                                                                  | 62.5 ms: 1.06x slower                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                       |
| logging_format          | 6.53 us                                                                  | 7.01 us: 1.07x slower                                       |
| generators              | 31.4 ms                                                                  | 33.8 ms: 1.08x slower                                       |
| logging_simple          | 6.12 us                                                                  | 6.61 us: 1.08x slower                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.46 ms: 1.10x slower                                       |
| pickle_dict             | 16.7 us                                                                  | 18.5 us: 1.11x slower                                       |
| unpack_sequence         | 39.4 ns                                                                  | 46.1 ns: 1.17x slower                                       |
| coverage                | 37.5 ms                                                                  | 55.9 ms: 1.49x slower                                       |
| Geometric mean          | (ref)                                                                    | 1.11x faster                                                |

Benchmark hidden because not significant (7): pickle, comprehensions, xml_etree_iterparse, nqueens, fannkuch, xml_etree_parse, json
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
