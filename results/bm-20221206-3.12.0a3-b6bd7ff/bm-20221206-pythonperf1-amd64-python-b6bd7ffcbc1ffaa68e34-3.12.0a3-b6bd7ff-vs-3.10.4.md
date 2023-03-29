
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: windows-amd64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 196 ms: 1.17x faster                                                       |
| chameleon      | 5.77 ms                                                                  | 4.53 ms: 1.28x faster                                                      |
| docutils       | 1.83 sec                                                                 | 1.56 sec: 1.17x faster                                                     |
| html5lib       | 47.3 ms                                                                  | 35.0 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 50.1 ms: 1.19x faster                                                      |
| nbody          | 71.5 ms                                                                  | 62.3 ms: 1.15x faster                                                      |
| pidigits       | 145 ms                                                                   | 151 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 82.5 ms: 1.25x faster                                                      |
| regex_dna      | 131 ms                                                                   | 120 ms: 1.09x faster                                                       |
| regex_v8       | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                                      |
| regex_effbot   | 1.64 ms                                                                  | 1.54 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.17 ms: 1.74x faster                                                      |
| unpickle_pure_python | 179 us                                                                   | 121 us: 1.48x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 179 us: 1.48x faster                                                       |
| xml_etree_process    | 43.0 ms                                                                  | 35.0 ms: 1.23x faster                                                      |
| unpickle             | 8.88 us                                                                  | 7.99 us: 1.11x faster                                                      |
| json_loads           | 14.2 us                                                                  | 12.9 us: 1.10x faster                                                      |
| xml_etree_generate   | 53.8 ms                                                                  | 49.7 ms: 1.08x faster                                                      |
| xml_etree_parse      | 95.6 ms                                                                  | 90.5 ms: 1.06x faster                                                      |
| unpickle_list        | 2.71 us                                                                  | 2.61 us: 1.04x faster                                                      |
| pickle               | 6.67 us                                                                  | 6.90 us: 1.03x slower                                                      |
| pickle_list          | 2.57 us                                                                  | 2.85 us: 1.11x slower                                                      |
| pickle_dict          | 16.7 us                                                                  | 19.4 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.13x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.5 ms: 1.04x faster                                                      |
| python_startup_no_site | 14.8 ms                                                                  | 15.7 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.19 ms: 1.40x faster                                                      |
| django_template | 29.2 ms                                                                  | 21.4 ms: 1.36x faster                                                      |
| genshi_text     | 18.5 ms                                                                  | 13.8 ms: 1.34x faster                                                      |
| genshi_xml      | 38.8 ms                                                                  | 32.3 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                                    | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.07 ms: 2.00x faster                                                      |
| json_dumps              | 9.00 ms                                                                  | 5.17 ms: 1.74x faster                                                      |
| go                      | 143 ms                                                                   | 84.8 ms: 1.69x faster                                                      |
| richards                | 41.0 ms                                                                  | 24.5 ms: 1.67x faster                                                      |
| logging_silent          | 94.6 ns                                                                  | 57.2 ns: 1.65x faster                                                      |
| scimark_sor             | 104 ms                                                                   | 64.6 ms: 1.60x faster                                                      |
| mypy2                   | 337 ms                                                                   | 215 ms: 1.57x faster                                                       |
| scimark_lu              | 83.9 ms                                                                  | 54.8 ms: 1.53x faster                                                      |
| raytrace                | 267 ms                                                                   | 179 ms: 1.49x faster                                                       |
| unpack_sequence         | 39.4 ns                                                                  | 26.4 ns: 1.49x faster                                                      |
| unpickle_pure_python    | 179 us                                                                   | 121 us: 1.48x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 179 us: 1.48x faster                                                       |
| pyflate                 | 388 ms                                                                   | 264 ms: 1.47x faster                                                       |
| scimark_monte_carlo     | 56.0 ms                                                                  | 38.1 ms: 1.47x faster                                                      |
| sqlglot_parse           | 1.22 ms                                                                  | 860 us: 1.42x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.19 ms: 1.40x faster                                                      |
| hexiom                  | 5.45 ms                                                                  | 3.89 ms: 1.40x faster                                                      |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.06 ms: 1.39x faster                                                      |
| django_template         | 29.2 ms                                                                  | 21.4 ms: 1.36x faster                                                      |
| crypto_pyaes            | 61.4 ms                                                                  | 45.1 ms: 1.36x faster                                                      |
| html5lib                | 47.3 ms                                                                  | 35.0 ms: 1.35x faster                                                      |
| chaos                   | 58.4 ms                                                                  | 43.2 ms: 1.35x faster                                                      |
| thrift                  | 632 us                                                                   | 469 us: 1.35x faster                                                       |
| genshi_text             | 18.5 ms                                                                  | 13.8 ms: 1.34x faster                                                      |
| deepcopy_memo           | 28.4 us                                                                  | 21.2 us: 1.34x faster                                                      |
| async_tree_io           | 1.02 sec                                                                 | 780 ms: 1.31x faster                                                       |
| async_tree_none         | 414 ms                                                                   | 317 ms: 1.31x faster                                                       |
| pprint_safe_repr        | 593 ms                                                                   | 458 ms: 1.30x faster                                                       |
| pprint_pformat          | 1.23 sec                                                                 | 947 ms: 1.30x faster                                                       |
| chameleon               | 5.77 ms                                                                  | 4.53 ms: 1.28x faster                                                      |
| pycparser               | 873 ms                                                                   | 691 ms: 1.26x faster                                                       |
| regex_compile           | 103 ms                                                                   | 82.5 ms: 1.25x faster                                                      |
| async_tree_memoization  | 485 ms                                                                   | 388 ms: 1.25x faster                                                       |
| xml_etree_process       | 43.0 ms                                                                  | 35.0 ms: 1.23x faster                                                      |
| spectral_norm           | 74.3 ms                                                                  | 61.4 ms: 1.21x faster                                                      |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.0 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 501 ms: 1.20x faster                                                       |
| dask                    | 310 ms                                                                   | 258 ms: 1.20x faster                                                       |
| genshi_xml              | 38.8 ms                                                                  | 32.3 ms: 1.20x faster                                                      |
| deepcopy                | 256 us                                                                   | 214 us: 1.20x faster                                                       |
| async_generators        | 214 ms                                                                   | 179 ms: 1.20x faster                                                       |
| float                   | 59.5 ms                                                                  | 50.1 ms: 1.19x faster                                                      |
| 2to3                    | 229 ms                                                                   | 196 ms: 1.17x faster                                                       |
| docutils                | 1.83 sec                                                                 | 1.56 sec: 1.17x faster                                                     |
| sqlglot_normalize       | 201 ms                                                                   | 172 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.30 ms: 1.16x faster                                                      |
| json                    | 3.18 ms                                                                  | 2.74 ms: 1.16x faster                                                      |
| deepcopy_reduce         | 2.18 us                                                                  | 1.88 us: 1.16x faster                                                      |
| nbody                   | 71.5 ms                                                                  | 62.3 ms: 1.15x faster                                                      |
| dulwich_log             | 47.0 ms                                                                  | 41.2 ms: 1.14x faster                                                      |
| bench_thread_pool       | 953 us                                                                   | 837 us: 1.14x faster                                                       |
| fannkuch                | 252 ms                                                                   | 222 ms: 1.13x faster                                                       |
| create_gc_cycles        | 764 us                                                                   | 682 us: 1.12x faster                                                       |
| nqueens                 | 64.8 ms                                                                  | 57.9 ms: 1.12x faster                                                      |
| unpickle                | 8.88 us                                                                  | 7.99 us: 1.11x faster                                                      |
| json_loads              | 14.2 us                                                                  | 12.9 us: 1.10x faster                                                      |
| sympy_integrate         | 14.7 ms                                                                  | 13.3 ms: 1.10x faster                                                      |
| sympy_expand            | 313 ms                                                                   | 286 ms: 1.09x faster                                                       |
| regex_dna               | 131 ms                                                                   | 120 ms: 1.09x faster                                                       |
| sympy_str               | 189 ms                                                                   | 173 ms: 1.09x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 49.7 ms: 1.08x faster                                                      |
| regex_v8                | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                                      |
| meteor_contest          | 74.3 ms                                                                  | 68.8 ms: 1.08x faster                                                      |
| sqlite_synth            | 1.85 us                                                                  | 1.73 us: 1.07x faster                                                      |
| regex_effbot            | 1.64 ms                                                                  | 1.54 ms: 1.06x faster                                                      |
| scimark_fft             | 187 ms                                                                   | 177 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 90.5 ms: 1.06x faster                                                      |
| pathlib                 | 75.2 ms                                                                  | 72.1 ms: 1.04x faster                                                      |
| python_startup          | 19.3 ms                                                                  | 18.5 ms: 1.04x faster                                                      |
| unpickle_list           | 2.71 us                                                                  | 2.61 us: 1.04x faster                                                      |
| coroutines              | 15.6 ms                                                                  | 15.1 ms: 1.04x faster                                                      |
| telco                   | 3.77 ms                                                                  | 3.64 ms: 1.03x faster                                                      |
| sympy_sum               | 102 ms                                                                   | 99.0 ms: 1.03x faster                                                      |
| comprehensions          | 16.0 us                                                                  | 15.5 us: 1.03x faster                                                      |
| logging_simple          | 6.12 us                                                                  | 6.22 us: 1.02x slower                                                      |
| logging_format          | 6.53 us                                                                  | 6.64 us: 1.02x slower                                                      |
| pickle                  | 6.67 us                                                                  | 6.90 us: 1.03x slower                                                      |
| pidigits                | 145 ms                                                                   | 151 ms: 1.04x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.7 ms: 1.06x slower                                                      |
| bench_mp_pool           | 59.2 ms                                                                  | 62.8 ms: 1.06x slower                                                      |
| generators              | 31.4 ms                                                                  | 33.9 ms: 1.08x slower                                                      |
| gc_traversal            | 1.33 ms                                                                  | 1.44 ms: 1.08x slower                                                      |
| asyncio_tcp             | 664 ms                                                                   | 735 ms: 1.11x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.85 us: 1.11x slower                                                      |
| pickle_dict             | 16.7 us                                                                  | 19.4 us: 1.16x slower                                                      |
| coverage                | 37.5 ms                                                                  | 51.6 ms: 1.38x slower                                                      |
| Geometric mean          | (ref)                                                                    | 1.19x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, mdp
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
