
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: windows-amd64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 211 ms: 1.09x faster                                            |
| chameleon      | 5.77 ms                                                                  | 5.59 ms: 1.03x faster                                           |
| docutils       | 1.83 sec                                                                 | 1.66 sec: 1.11x faster                                          |
| html5lib       | 47.3 ms                                                                  | 41.4 ms: 1.14x faster                                           |
| tornado_http   | 106 ms                                                                   | 95.3 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 54.5 ms: 1.09x faster                                           |
| nbody          | 71.5 ms                                                                  | 70.1 ms: 1.02x faster                                           |
| pidigits       | 145 ms                                                                   | 153 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.64 ms                                                                  | 1.39 ms: 1.18x faster                                           |
| regex_dna      | 131 ms                                                                   | 120 ms: 1.09x faster                                            |
| regex_compile  | 103 ms                                                                   | 97.0 ms: 1.07x faster                                           |
| regex_v8       | 15.1 ms                                                                  | 14.4 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 264 us                                                                   | 216 us: 1.22x faster                                            |
| xml_etree_process    | 43.0 ms                                                                  | 39.1 ms: 1.10x faster                                           |
| unpickle             | 8.88 us                                                                  | 8.07 us: 1.10x faster                                           |
| json_dumps           | 9.00 ms                                                                  | 8.21 ms: 1.10x faster                                           |
| unpickle_pure_python | 179 us                                                                   | 164 us: 1.09x faster                                            |
| xml_etree_iterparse  | 62.5 ms                                                                  | 62.0 ms: 1.01x faster                                           |
| json_loads           | 14.2 us                                                                  | 14.1 us: 1.01x faster                                           |
| xml_etree_generate   | 53.8 ms                                                                  | 54.1 ms: 1.01x slower                                           |
| pickle               | 6.67 us                                                                  | 6.74 us: 1.01x slower                                           |
| xml_etree_parse      | 95.6 ms                                                                  | 96.7 ms: 1.01x slower                                           |
| unpickle_list        | 2.71 us                                                                  | 2.76 us: 1.02x slower                                           |
| pickle_list          | 2.57 us                                                                  | 2.64 us: 1.03x slower                                           |
| pickle_dict          | 16.7 us                                                                  | 17.4 us: 1.04x slower                                           |
| Geometric mean       | (ref)                                                                    | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 19.0 ms: 1.01x faster                                           |
| python_startup_no_site | 14.8 ms                                                                  | 15.8 ms: 1.07x slower                                           |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 25.1 ms: 1.16x faster                                           |
| mako            | 8.69 ms                                                                  | 7.62 ms: 1.14x faster                                           |
| genshi_text     | 18.5 ms                                                                  | 17.9 ms: 1.04x faster                                           |
| genshi_xml      | 38.8 ms                                                                  | 40.2 ms: 1.04x slower                                           |
| Geometric mean  | (ref)                                                                    | 1.07x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.72 ms: 1.52x faster                                           |
| go                      | 143 ms                                                                   | 100 ms: 1.43x faster                                            |
| logging_silent          | 94.6 ns                                                                  | 72.2 ns: 1.31x faster                                           |
| scimark_lu              | 83.9 ms                                                                  | 64.6 ms: 1.30x faster                                           |
| richards                | 41.0 ms                                                                  | 31.6 ms: 1.30x faster                                           |
| scimark_sor             | 104 ms                                                                   | 80.0 ms: 1.29x faster                                           |
| async_tree_io           | 1.02 sec                                                                 | 794 ms: 1.29x faster                                            |
| raytrace                | 267 ms                                                                   | 213 ms: 1.25x faster                                            |
| pyflate                 | 388 ms                                                                   | 314 ms: 1.24x faster                                            |
| async_tree_none         | 414 ms                                                                   | 336 ms: 1.23x faster                                            |
| thrift                  | 632 us                                                                   | 516 us: 1.23x faster                                            |
| pickle_pure_python      | 264 us                                                                   | 216 us: 1.22x faster                                            |
| scimark_monte_carlo     | 56.0 ms                                                                  | 46.0 ms: 1.22x faster                                           |
| async_tree_memoization  | 485 ms                                                                   | 400 ms: 1.21x faster                                            |
| crypto_pyaes            | 61.4 ms                                                                  | 51.8 ms: 1.18x faster                                           |
| regex_effbot            | 1.64 ms                                                                  | 1.39 ms: 1.18x faster                                           |
| pycparser               | 873 ms                                                                   | 750 ms: 1.16x faster                                            |
| django_template         | 29.2 ms                                                                  | 25.1 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 520 ms: 1.16x faster                                            |
| sqlalchemy_declarative  | 96.4 ms                                                                  | 83.2 ms: 1.16x faster                                           |
| async_generators        | 214 ms                                                                   | 187 ms: 1.15x faster                                            |
| mypy2                   | 337 ms                                                                   | 295 ms: 1.14x faster                                            |
| html5lib                | 47.3 ms                                                                  | 41.4 ms: 1.14x faster                                           |
| mako                    | 8.69 ms                                                                  | 7.62 ms: 1.14x faster                                           |
| create_gc_cycles        | 764 us                                                                   | 675 us: 1.13x faster                                            |
| chaos                   | 58.4 ms                                                                  | 51.8 ms: 1.13x faster                                           |
| hexiom                  | 5.45 ms                                                                  | 4.84 ms: 1.13x faster                                           |
| tornado_http            | 106 ms                                                                   | 95.3 ms: 1.12x faster                                           |
| dask                    | 310 ms                                                                   | 280 ms: 1.11x faster                                            |
| docutils                | 1.83 sec                                                                 | 1.66 sec: 1.11x faster                                          |
| pprint_pformat          | 1.23 sec                                                                 | 1.11 sec: 1.10x faster                                          |
| xml_etree_process       | 43.0 ms                                                                  | 39.1 ms: 1.10x faster                                           |
| unpickle                | 8.88 us                                                                  | 8.07 us: 1.10x faster                                           |
| json_dumps              | 9.00 ms                                                                  | 8.21 ms: 1.10x faster                                           |
| regex_dna               | 131 ms                                                                   | 120 ms: 1.09x faster                                            |
| unpickle_pure_python    | 179 us                                                                   | 164 us: 1.09x faster                                            |
| float                   | 59.5 ms                                                                  | 54.5 ms: 1.09x faster                                           |
| deepcopy_memo           | 28.4 us                                                                  | 26.1 us: 1.09x faster                                           |
| 2to3                    | 229 ms                                                                   | 211 ms: 1.09x faster                                            |
| pprint_safe_repr        | 593 ms                                                                   | 548 ms: 1.08x faster                                            |
| sqlalchemy_imperative   | 11.3 ms                                                                  | 10.5 ms: 1.08x faster                                           |
| sqlite_synth            | 1.85 us                                                                  | 1.71 us: 1.08x faster                                           |
| bench_thread_pool       | 953 us                                                                   | 889 us: 1.07x faster                                            |
| regex_compile           | 103 ms                                                                   | 97.0 ms: 1.07x faster                                           |
| spectral_norm           | 74.3 ms                                                                  | 70.6 ms: 1.05x faster                                           |
| aiohttp                 | 968 us                                                                   | 921 us: 1.05x faster                                            |
| regex_v8                | 15.1 ms                                                                  | 14.4 ms: 1.05x faster                                           |
| genshi_text             | 18.5 ms                                                                  | 17.9 ms: 1.04x faster                                           |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.42 ms: 1.04x faster                                           |
| chameleon               | 5.77 ms                                                                  | 5.59 ms: 1.03x faster                                           |
| sqlglot_optimize        | 38.7 ms                                                                  | 37.5 ms: 1.03x faster                                           |
| sympy_integrate         | 14.7 ms                                                                  | 14.2 ms: 1.03x faster                                           |
| logging_simple          | 6.12 us                                                                  | 5.94 us: 1.03x faster                                           |
| logging_format          | 6.53 us                                                                  | 6.39 us: 1.02x faster                                           |
| nbody                   | 71.5 ms                                                                  | 70.1 ms: 1.02x faster                                           |
| pylint                  | 337 ms                                                                   | 331 ms: 1.02x faster                                            |
| dulwich_log             | 47.0 ms                                                                  | 46.1 ms: 1.02x faster                                           |
| python_startup          | 19.3 ms                                                                  | 19.0 ms: 1.01x faster                                           |
| sqlglot_parse           | 1.22 ms                                                                  | 1.21 ms: 1.01x faster                                           |
| xml_etree_iterparse     | 62.5 ms                                                                  | 62.0 ms: 1.01x faster                                           |
| json_loads              | 14.2 us                                                                  | 14.1 us: 1.01x faster                                           |
| xml_etree_generate      | 53.8 ms                                                                  | 54.1 ms: 1.01x slower                                           |
| sqlglot_normalize       | 201 ms                                                                   | 203 ms: 1.01x slower                                            |
| pickle                  | 6.67 us                                                                  | 6.74 us: 1.01x slower                                           |
| xml_etree_parse         | 95.6 ms                                                                  | 96.7 ms: 1.01x slower                                           |
| unpickle_list           | 2.71 us                                                                  | 2.76 us: 1.02x slower                                           |
| deepcopy                | 256 us                                                                   | 261 us: 1.02x slower                                            |
| scimark_fft             | 187 ms                                                                   | 191 ms: 1.02x slower                                            |
| pickle_list             | 2.57 us                                                                  | 2.64 us: 1.03x slower                                           |
| genshi_xml              | 38.8 ms                                                                  | 40.2 ms: 1.04x slower                                           |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.77 ms: 1.04x slower                                           |
| pickle_dict             | 16.7 us                                                                  | 17.4 us: 1.04x slower                                           |
| pidigits                | 145 ms                                                                   | 153 ms: 1.05x slower                                            |
| fannkuch                | 252 ms                                                                   | 266 ms: 1.06x slower                                            |
| meteor_contest          | 74.3 ms                                                                  | 78.7 ms: 1.06x slower                                           |
| nqueens                 | 64.8 ms                                                                  | 68.9 ms: 1.06x slower                                           |
| python_startup_no_site  | 14.8 ms                                                                  | 15.8 ms: 1.07x slower                                           |
| bench_mp_pool           | 59.2 ms                                                                  | 63.3 ms: 1.07x slower                                           |
| telco                   | 3.77 ms                                                                  | 4.05 ms: 1.07x slower                                           |
| mdp                     | 1.60 sec                                                                 | 1.75 sec: 1.09x slower                                          |
| gc_traversal            | 1.33 ms                                                                  | 1.46 ms: 1.09x slower                                           |
| asyncio_tcp             | 664 ms                                                                   | 742 ms: 1.12x slower                                            |
| unpack_sequence         | 39.4 ns                                                                  | 44.3 ns: 1.13x slower                                           |
| comprehensions          | 16.0 us                                                                  | 18.2 us: 1.14x slower                                           |
| generators              | 31.4 ms                                                                  | 35.7 ms: 1.14x slower                                           |
| coverage                | 37.5 ms                                                                  | 106 ms: 2.82x slower                                            |
| Geometric mean          | (ref)                                                                    | 1.05x faster                                                    |

Benchmark hidden because not significant (7): pathlib, coroutines, sympy_expand, sympy_sum, deepcopy_reduce, sympy_str, json
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging
