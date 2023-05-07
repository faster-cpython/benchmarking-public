
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 207 ms: 1.11x faster                                        |
| docutils       | 1.83 sec                                                                 | 1.58 sec: 1.16x faster                                      |
| tornado_http   | 106 ms                                                                   | 88.3 ms: 1.21x faster                                       |
| Geometric mean | (ref)                                                                    | 1.16x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 51.7 ms: 1.15x faster                                       |
| nbody          | 71.5 ms                                                                  | 69.4 ms: 1.03x faster                                       |
| pidigits       | 145 ms                                                                   | 151 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 84.5 ms: 1.22x faster                                       |
| regex_dna      | 131 ms                                                                   | 119 ms: 1.10x faster                                        |
| regex_v8       | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                       |
| regex_effbot   | 1.64 ms                                                                  | 1.62 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.63 ms: 1.60x faster                                       |
| pickle_pure_python   | 264 us                                                                   | 190 us: 1.39x faster                                        |
| unpickle_pure_python | 179 us                                                                   | 134 us: 1.34x faster                                        |
| xml_etree_process    | 43.0 ms                                                                  | 38.2 ms: 1.13x faster                                       |
| unpickle             | 8.88 us                                                                  | 8.29 us: 1.07x faster                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 92.1 ms: 1.04x faster                                       |
| json_loads           | 14.2 us                                                                  | 13.9 us: 1.02x faster                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 63.1 ms: 1.01x slower                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 55.9 ms: 1.04x slower                                       |
| unpickle_list        | 2.71 us                                                                  | 2.86 us: 1.05x slower                                       |
| pickle               | 6.67 us                                                                  | 7.04 us: 1.06x slower                                       |
| pickle_dict          | 16.7 us                                                                  | 18.1 us: 1.08x slower                                       |
| pickle_list          | 2.57 us                                                                  | 2.83 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                                    | 1.08x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.4 ms: 1.05x faster                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.6 ms: 1.05x slower                                       |
| Geometric mean         | (ref)                                                                    | 1.00x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.69 ms                                                                  | 6.48 ms: 1.34x faster                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.04 ms: 2.03x faster                                       |
| go                      | 143 ms                                                                   | 86.0 ms: 1.67x faster                                       |
| richards                | 41.0 ms                                                                  | 25.1 ms: 1.64x faster                                       |
| logging_silent          | 94.6 ns                                                                  | 58.0 ns: 1.63x faster                                       |
| json_dumps              | 9.00 ms                                                                  | 5.63 ms: 1.60x faster                                       |
| mypy2                   | 337 ms                                                                   | 217 ms: 1.56x faster                                        |
| generators              | 31.4 ms                                                                  | 20.3 ms: 1.55x faster                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 787 us: 1.55x faster                                        |
| scimark_lu              | 83.9 ms                                                                  | 56.4 ms: 1.49x faster                                       |
| sqlglot_transpile       | 1.47 ms                                                                  | 996 us: 1.48x faster                                        |
| asyncio_tcp             | 664 ms                                                                   | 454 ms: 1.46x faster                                        |
| raytrace                | 267 ms                                                                   | 184 ms: 1.45x faster                                        |
| async_tree_io           | 1.02 sec                                                                 | 716 ms: 1.43x faster                                        |
| pickle_pure_python      | 264 us                                                                   | 190 us: 1.39x faster                                        |
| async_tree_memoization  | 485 ms                                                                   | 351 ms: 1.38x faster                                        |
| hexiom                  | 5.45 ms                                                                  | 3.95 ms: 1.38x faster                                       |
| async_tree_none         | 414 ms                                                                   | 300 ms: 1.38x faster                                        |
| pyflate                 | 388 ms                                                                   | 284 ms: 1.37x faster                                        |
| unpickle_pure_python    | 179 us                                                                   | 134 us: 1.34x faster                                        |
| mako                    | 8.69 ms                                                                  | 6.48 ms: 1.34x faster                                       |
| chaos                   | 58.4 ms                                                                  | 43.8 ms: 1.33x faster                                       |
| crypto_pyaes            | 61.4 ms                                                                  | 46.3 ms: 1.33x faster                                       |
| pycparser               | 873 ms                                                                   | 664 ms: 1.32x faster                                        |
| scimark_sor             | 104 ms                                                                   | 78.7 ms: 1.31x faster                                       |
| scimark_monte_carlo     | 56.0 ms                                                                  | 43.1 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 468 ms: 1.29x faster                                        |
| regex_compile           | 103 ms                                                                   | 84.5 ms: 1.22x faster                                       |
| tornado_http            | 106 ms                                                                   | 88.3 ms: 1.21x faster                                       |
| spectral_norm           | 74.3 ms                                                                  | 61.7 ms: 1.20x faster                                       |
| deepcopy_memo           | 28.4 us                                                                  | 23.9 us: 1.19x faster                                       |
| pprint_pformat          | 1.23 sec                                                                 | 1.03 sec: 1.19x faster                                      |
| pprint_safe_repr        | 593 ms                                                                   | 509 ms: 1.17x faster                                        |
| docutils                | 1.83 sec                                                                 | 1.58 sec: 1.16x faster                                      |
| float                   | 59.5 ms                                                                  | 51.7 ms: 1.15x faster                                       |
| bench_thread_pool       | 953 us                                                                   | 837 us: 1.14x faster                                        |
| xml_etree_process       | 43.0 ms                                                                  | 38.2 ms: 1.13x faster                                       |
| mdp                     | 1.60 sec                                                                 | 1.42 sec: 1.13x faster                                      |
| coroutines              | 15.6 ms                                                                  | 13.9 ms: 1.12x faster                                       |
| nqueens                 | 64.8 ms                                                                  | 57.9 ms: 1.12x faster                                       |
| dulwich_log             | 47.0 ms                                                                  | 42.0 ms: 1.12x faster                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.39 ms: 1.12x faster                                       |
| json                    | 3.18 ms                                                                  | 2.85 ms: 1.11x faster                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 34.9 ms: 1.11x faster                                       |
| 2to3                    | 229 ms                                                                   | 207 ms: 1.11x faster                                        |
| create_gc_cycles        | 764 us                                                                   | 693 us: 1.10x faster                                        |
| deepcopy                | 256 us                                                                   | 233 us: 1.10x faster                                        |
| regex_dna               | 131 ms                                                                   | 119 ms: 1.10x faster                                        |
| regex_v8                | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.71 us: 1.08x faster                                       |
| unpickle                | 8.88 us                                                                  | 8.29 us: 1.07x faster                                       |
| scimark_fft             | 187 ms                                                                   | 175 ms: 1.07x faster                                        |
| sqlglot_normalize       | 201 ms                                                                   | 191 ms: 1.05x faster                                        |
| deepcopy_reduce         | 2.18 us                                                                  | 2.08 us: 1.05x faster                                       |
| python_startup          | 19.3 ms                                                                  | 18.4 ms: 1.05x faster                                       |
| unpack_sequence         | 39.4 ns                                                                  | 37.8 ns: 1.04x faster                                       |
| fannkuch                | 252 ms                                                                   | 242 ms: 1.04x faster                                        |
| xml_etree_parse         | 95.6 ms                                                                  | 92.1 ms: 1.04x faster                                       |
| nbody                   | 71.5 ms                                                                  | 69.4 ms: 1.03x faster                                       |
| comprehensions          | 16.0 us                                                                  | 15.5 us: 1.03x faster                                       |
| meteor_contest          | 74.3 ms                                                                  | 72.6 ms: 1.02x faster                                       |
| json_loads              | 14.2 us                                                                  | 13.9 us: 1.02x faster                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.62 ms: 1.02x faster                                       |
| xml_etree_iterparse     | 62.5 ms                                                                  | 63.1 ms: 1.01x slower                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 55.9 ms: 1.04x slower                                       |
| pidigits                | 145 ms                                                                   | 151 ms: 1.04x slower                                        |
| logging_simple          | 6.12 us                                                                  | 6.39 us: 1.04x slower                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.6 ms: 1.05x slower                                       |
| unpickle_list           | 2.71 us                                                                  | 2.86 us: 1.05x slower                                       |
| pickle                  | 6.67 us                                                                  | 7.04 us: 1.06x slower                                       |
| telco                   | 3.77 ms                                                                  | 4.00 ms: 1.06x slower                                       |
| logging_format          | 6.53 us                                                                  | 6.94 us: 1.06x slower                                       |
| pathlib                 | 75.2 ms                                                                  | 81.2 ms: 1.08x slower                                       |
| pickle_dict             | 16.7 us                                                                  | 18.1 us: 1.08x slower                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.46 ms: 1.09x slower                                       |
| async_generators        | 214 ms                                                                   | 235 ms: 1.10x slower                                        |
| pickle_list             | 2.57 us                                                                  | 2.83 us: 1.10x slower                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 66.3 ms: 1.12x slower                                       |
| dask                    | 310 ms                                                                   | 360 ms: 1.16x slower                                        |
| coverage                | 37.5 ms                                                                  | 53.8 ms: 1.44x slower                                       |
| Geometric mean          | (ref)                                                                    | 1.16x faster                                                |
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
