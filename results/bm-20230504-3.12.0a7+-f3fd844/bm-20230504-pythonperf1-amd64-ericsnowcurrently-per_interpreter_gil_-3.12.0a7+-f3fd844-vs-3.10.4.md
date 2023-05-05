
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: windows-amd64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 208 ms: 1.10x faster                                                                   |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                                                 |
| tornado_http   | 106 ms                                                                   | 89.0 ms: 1.20x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.15x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 52.1 ms: 1.14x faster                                                                  |
| nbody          | 71.5 ms                                                                  | 68.6 ms: 1.04x faster                                                                  |
| pidigits       | 145 ms                                                                   | 150 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.05x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 85.1 ms: 1.22x faster                                                                  |
| regex_dna      | 131 ms                                                                   | 116 ms: 1.13x faster                                                                   |
| regex_v8       | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.60 ms: 1.61x faster                                                                  |
| pickle_pure_python   | 264 us                                                                   | 191 us: 1.38x faster                                                                   |
| unpickle_pure_python | 179 us                                                                   | 136 us: 1.32x faster                                                                   |
| xml_etree_process    | 43.0 ms                                                                  | 37.2 ms: 1.16x faster                                                                  |
| unpickle             | 8.88 us                                                                  | 8.46 us: 1.05x faster                                                                  |
| xml_etree_parse      | 95.6 ms                                                                  | 91.3 ms: 1.05x faster                                                                  |
| xml_etree_iterparse  | 62.5 ms                                                                  | 61.1 ms: 1.02x faster                                                                  |
| xml_etree_generate   | 53.8 ms                                                                  | 54.6 ms: 1.01x slower                                                                  |
| unpickle_list        | 2.71 us                                                                  | 2.82 us: 1.04x slower                                                                  |
| pickle               | 6.67 us                                                                  | 6.95 us: 1.04x slower                                                                  |
| pickle_list          | 2.57 us                                                                  | 2.76 us: 1.08x slower                                                                  |
| pickle_dict          | 16.7 us                                                                  | 18.1 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.8 ms: 1.02x faster                                                                  |
| python_startup_no_site | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.02x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 8.69 ms                                                                  | 6.60 ms: 1.32x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.05 ms: 2.02x faster                                                                  |
| go                      | 143 ms                                                                   | 87.9 ms: 1.63x faster                                                                  |
| logging_silent          | 94.6 ns                                                                  | 58.1 ns: 1.63x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.60 ms: 1.61x faster                                                                  |
| richards                | 41.0 ms                                                                  | 25.7 ms: 1.60x faster                                                                  |
| mypy2                   | 337 ms                                                                   | 214 ms: 1.58x faster                                                                   |
| sqlglot_parse           | 1.22 ms                                                                  | 791 us: 1.54x faster                                                                   |
| generators              | 31.4 ms                                                                  | 20.7 ms: 1.52x faster                                                                  |
| scimark_lu              | 83.9 ms                                                                  | 56.8 ms: 1.48x faster                                                                  |
| sqlglot_transpile       | 1.47 ms                                                                  | 999 us: 1.47x faster                                                                   |
| asyncio_tcp             | 664 ms                                                                   | 456 ms: 1.46x faster                                                                   |
| raytrace                | 267 ms                                                                   | 185 ms: 1.44x faster                                                                   |
| async_tree_none         | 414 ms                                                                   | 289 ms: 1.43x faster                                                                   |
| async_tree_memoization  | 485 ms                                                                   | 341 ms: 1.42x faster                                                                   |
| async_tree_io           | 1.02 sec                                                                 | 727 ms: 1.41x faster                                                                   |
| pickle_pure_python      | 264 us                                                                   | 191 us: 1.38x faster                                                                   |
| hexiom                  | 5.45 ms                                                                  | 3.99 ms: 1.37x faster                                                                  |
| pyflate                 | 388 ms                                                                   | 289 ms: 1.34x faster                                                                   |
| scimark_sor             | 104 ms                                                                   | 78.1 ms: 1.32x faster                                                                  |
| unpickle_pure_python    | 179 us                                                                   | 136 us: 1.32x faster                                                                   |
| mako                    | 8.69 ms                                                                  | 6.60 ms: 1.32x faster                                                                  |
| pycparser               | 873 ms                                                                   | 666 ms: 1.31x faster                                                                   |
| chaos                   | 58.4 ms                                                                  | 44.8 ms: 1.31x faster                                                                  |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 464 ms: 1.30x faster                                                                   |
| crypto_pyaes            | 61.4 ms                                                                  | 47.4 ms: 1.30x faster                                                                  |
| scimark_monte_carlo     | 56.0 ms                                                                  | 43.3 ms: 1.29x faster                                                                  |
| regex_compile           | 103 ms                                                                   | 85.1 ms: 1.22x faster                                                                  |
| tornado_http            | 106 ms                                                                   | 89.0 ms: 1.20x faster                                                                  |
| deepcopy_memo           | 28.4 us                                                                  | 23.9 us: 1.19x faster                                                                  |
| pprint_pformat          | 1.23 sec                                                                 | 1.04 sec: 1.19x faster                                                                 |
| pprint_safe_repr        | 593 ms                                                                   | 511 ms: 1.16x faster                                                                   |
| xml_etree_process       | 43.0 ms                                                                  | 37.2 ms: 1.16x faster                                                                  |
| spectral_norm           | 74.3 ms                                                                  | 64.3 ms: 1.15x faster                                                                  |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                                                 |
| float                   | 59.5 ms                                                                  | 52.1 ms: 1.14x faster                                                                  |
| sqlglot_optimize        | 38.7 ms                                                                  | 34.0 ms: 1.14x faster                                                                  |
| create_gc_cycles        | 764 us                                                                   | 676 us: 1.13x faster                                                                   |
| bench_thread_pool       | 953 us                                                                   | 843 us: 1.13x faster                                                                   |
| mdp                     | 1.60 sec                                                                 | 1.42 sec: 1.13x faster                                                                 |
| regex_dna               | 131 ms                                                                   | 116 ms: 1.13x faster                                                                   |
| coroutines              | 15.6 ms                                                                  | 14.0 ms: 1.12x faster                                                                  |
| 2to3                    | 229 ms                                                                   | 208 ms: 1.10x faster                                                                   |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.42 ms: 1.10x faster                                                                  |
| deepcopy                | 256 us                                                                   | 234 us: 1.09x faster                                                                   |
| dulwich_log             | 47.0 ms                                                                  | 43.1 ms: 1.09x faster                                                                  |
| sqlglot_normalize       | 201 ms                                                                   | 185 ms: 1.08x faster                                                                   |
| nqueens                 | 64.8 ms                                                                  | 59.9 ms: 1.08x faster                                                                  |
| sqlite_synth            | 1.85 us                                                                  | 1.71 us: 1.08x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.96 ms: 1.08x faster                                                                  |
| regex_v8                | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| scimark_fft             | 187 ms                                                                   | 174 ms: 1.07x faster                                                                   |
| deepcopy_reduce         | 2.18 us                                                                  | 2.07 us: 1.06x faster                                                                  |
| unpickle                | 8.88 us                                                                  | 8.46 us: 1.05x faster                                                                  |
| xml_etree_parse         | 95.6 ms                                                                  | 91.3 ms: 1.05x faster                                                                  |
| regex_effbot            | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                                                  |
| nbody                   | 71.5 ms                                                                  | 68.6 ms: 1.04x faster                                                                  |
| fannkuch                | 252 ms                                                                   | 244 ms: 1.03x faster                                                                   |
| python_startup          | 19.3 ms                                                                  | 18.8 ms: 1.02x faster                                                                  |
| xml_etree_iterparse     | 62.5 ms                                                                  | 61.1 ms: 1.02x faster                                                                  |
| xml_etree_generate      | 53.8 ms                                                                  | 54.6 ms: 1.01x slower                                                                  |
| pidigits                | 145 ms                                                                   | 150 ms: 1.03x slower                                                                   |
| unpickle_list           | 2.71 us                                                                  | 2.82 us: 1.04x slower                                                                  |
| pickle                  | 6.67 us                                                                  | 6.95 us: 1.04x slower                                                                  |
| logging_simple          | 6.12 us                                                                  | 6.51 us: 1.06x slower                                                                  |
| meteor_contest          | 74.3 ms                                                                  | 79.0 ms: 1.06x slower                                                                  |
| async_generators        | 214 ms                                                                   | 228 ms: 1.06x slower                                                                   |
| python_startup_no_site  | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                                                  |
| gc_traversal            | 1.33 ms                                                                  | 1.43 ms: 1.07x slower                                                                  |
| unpack_sequence         | 39.4 ns                                                                  | 42.2 ns: 1.07x slower                                                                  |
| logging_format          | 6.53 us                                                                  | 7.03 us: 1.08x slower                                                                  |
| pickle_list             | 2.57 us                                                                  | 2.76 us: 1.08x slower                                                                  |
| pickle_dict             | 16.7 us                                                                  | 18.1 us: 1.08x slower                                                                  |
| pathlib                 | 75.2 ms                                                                  | 81.7 ms: 1.09x slower                                                                  |
| telco                   | 3.77 ms                                                                  | 4.14 ms: 1.10x slower                                                                  |
| bench_mp_pool           | 59.2 ms                                                                  | 67.1 ms: 1.13x slower                                                                  |
| dask                    | 310 ms                                                                   | 366 ms: 1.18x slower                                                                   |
| coverage                | 37.5 ms                                                                  | 52.3 ms: 1.40x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.15x faster                                                                           |

Benchmark hidden because not significant (2): comprehensions, json_loads
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
