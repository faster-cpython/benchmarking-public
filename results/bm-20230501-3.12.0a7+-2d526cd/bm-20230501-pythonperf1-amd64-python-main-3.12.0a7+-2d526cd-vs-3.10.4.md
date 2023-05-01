
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 207 ms: 1.11x faster                                        |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                      |
| html5lib       | 47.3 ms                                                                  | 36.1 ms: 1.31x faster                                       |
| tornado_http   | 106 ms                                                                   | 87.3 ms: 1.22x faster                                       |
| Geometric mean | (ref)                                                                    | 1.19x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 52.2 ms: 1.14x faster                                       |
| nbody          | 71.5 ms                                                                  | 67.3 ms: 1.06x faster                                       |
| pidigits       | 145 ms                                                                   | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                    | 1.06x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 85.6 ms: 1.21x faster                                       |
| regex_dna      | 131 ms                                                                   | 117 ms: 1.12x faster                                        |
| regex_v8       | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                       |
| regex_effbot   | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                                    | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.55 ms: 1.62x faster                                       |
| pickle_pure_python   | 264 us                                                                   | 191 us: 1.38x faster                                        |
| unpickle_pure_python | 179 us                                                                   | 135 us: 1.33x faster                                        |
| xml_etree_process    | 43.0 ms                                                                  | 37.8 ms: 1.14x faster                                       |
| json_loads           | 14.2 us                                                                  | 13.3 us: 1.06x faster                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 91.5 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 61.3 ms: 1.02x faster                                       |
| unpickle             | 8.88 us                                                                  | 8.73 us: 1.02x faster                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 54.6 ms: 1.01x slower                                       |
| unpickle_list        | 2.71 us                                                                  | 2.80 us: 1.03x slower                                       |
| pickle               | 6.67 us                                                                  | 7.02 us: 1.05x slower                                       |
| pickle_dict          | 16.7 us                                                                  | 18.1 us: 1.08x slower                                       |
| pickle_list          | 2.57 us                                                                  | 2.85 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.3 ms: 1.05x faster                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                       |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 8.69 ms                                                                  | 6.67 ms: 1.30x faster                                       |
| genshi_text    | 18.5 ms                                                                  | 14.9 ms: 1.24x faster                                       |
| genshi_xml     | 38.8 ms                                                                  | 32.5 ms: 1.19x faster                                       |
| Geometric mean | (ref)                                                                    | 1.24x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.12 ms: 1.96x faster                                       |
| go                      | 143 ms                                                                   | 86.6 ms: 1.65x faster                                       |
| json_dumps              | 9.00 ms                                                                  | 5.55 ms: 1.62x faster                                       |
| richards                | 41.0 ms                                                                  | 25.6 ms: 1.60x faster                                       |
| logging_silent          | 94.6 ns                                                                  | 60.2 ns: 1.57x faster                                       |
| mypy2                   | 337 ms                                                                   | 215 ms: 1.57x faster                                        |
| sqlglot_parse           | 1.22 ms                                                                  | 791 us: 1.54x faster                                        |
| scimark_lu              | 83.9 ms                                                                  | 56.8 ms: 1.48x faster                                       |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.01 ms: 1.46x faster                                       |
| generators              | 31.4 ms                                                                  | 21.6 ms: 1.46x faster                                       |
| asyncio_tcp             | 664 ms                                                                   | 463 ms: 1.43x faster                                        |
| async_tree_io           | 1.02 sec                                                                 | 724 ms: 1.41x faster                                        |
| raytrace                | 267 ms                                                                   | 191 ms: 1.40x faster                                        |
| async_tree_none         | 414 ms                                                                   | 297 ms: 1.39x faster                                        |
| async_tree_memoization  | 485 ms                                                                   | 350 ms: 1.39x faster                                        |
| pickle_pure_python      | 264 us                                                                   | 191 us: 1.38x faster                                        |
| hexiom                  | 5.45 ms                                                                  | 4.06 ms: 1.34x faster                                       |
| unpickle_pure_python    | 179 us                                                                   | 135 us: 1.33x faster                                        |
| pyflate                 | 388 ms                                                                   | 295 ms: 1.32x faster                                        |
| pycparser               | 873 ms                                                                   | 665 ms: 1.31x faster                                        |
| chaos                   | 58.4 ms                                                                  | 44.6 ms: 1.31x faster                                       |
| html5lib                | 47.3 ms                                                                  | 36.1 ms: 1.31x faster                                       |
| scimark_sor             | 104 ms                                                                   | 79.1 ms: 1.31x faster                                       |
| mako                    | 8.69 ms                                                                  | 6.67 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 473 ms: 1.28x faster                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 48.1 ms: 1.28x faster                                       |
| thrift                  | 632 us                                                                   | 508 us: 1.24x faster                                        |
| scimark_monte_carlo     | 56.0 ms                                                                  | 45.1 ms: 1.24x faster                                       |
| genshi_text             | 18.5 ms                                                                  | 14.9 ms: 1.24x faster                                       |
| tornado_http            | 106 ms                                                                   | 87.3 ms: 1.22x faster                                       |
| regex_compile           | 103 ms                                                                   | 85.6 ms: 1.21x faster                                       |
| pprint_pformat          | 1.23 sec                                                                 | 1.02 sec: 1.20x faster                                      |
| genshi_xml              | 38.8 ms                                                                  | 32.5 ms: 1.19x faster                                       |
| deepcopy_memo           | 28.4 us                                                                  | 23.9 us: 1.19x faster                                       |
| pprint_safe_repr        | 593 ms                                                                   | 505 ms: 1.18x faster                                        |
| bench_thread_pool       | 953 us                                                                   | 827 us: 1.15x faster                                        |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                      |
| sqlglot_optimize        | 38.7 ms                                                                  | 33.8 ms: 1.14x faster                                       |
| float                   | 59.5 ms                                                                  | 52.2 ms: 1.14x faster                                       |
| xml_etree_process       | 43.0 ms                                                                  | 37.8 ms: 1.14x faster                                       |
| spectral_norm           | 74.3 ms                                                                  | 65.4 ms: 1.14x faster                                       |
| create_gc_cycles        | 764 us                                                                   | 675 us: 1.13x faster                                        |
| regex_dna               | 131 ms                                                                   | 117 ms: 1.12x faster                                        |
| mdp                     | 1.60 sec                                                                 | 1.43 sec: 1.12x faster                                      |
| regex_v8                | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                       |
| 2to3                    | 229 ms                                                                   | 207 ms: 1.11x faster                                        |
| dulwich_log             | 47.0 ms                                                                  | 42.7 ms: 1.10x faster                                       |
| coroutines              | 15.6 ms                                                                  | 14.2 ms: 1.10x faster                                       |
| deepcopy                | 256 us                                                                   | 233 us: 1.10x faster                                        |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.45 ms: 1.09x faster                                       |
| sqlglot_normalize       | 201 ms                                                                   | 185 ms: 1.08x faster                                        |
| sqlite_synth            | 1.85 us                                                                  | 1.71 us: 1.08x faster                                       |
| nqueens                 | 64.8 ms                                                                  | 60.6 ms: 1.07x faster                                       |
| json_loads              | 14.2 us                                                                  | 13.3 us: 1.06x faster                                       |
| nbody                   | 71.5 ms                                                                  | 67.3 ms: 1.06x faster                                       |
| json                    | 3.18 ms                                                                  | 3.02 ms: 1.05x faster                                       |
| python_startup          | 19.3 ms                                                                  | 18.3 ms: 1.05x faster                                       |
| deepcopy_reduce         | 2.18 us                                                                  | 2.07 us: 1.05x faster                                       |
| fannkuch                | 252 ms                                                                   | 240 ms: 1.05x faster                                        |
| scimark_fft             | 187 ms                                                                   | 179 ms: 1.05x faster                                        |
| xml_etree_parse         | 95.6 ms                                                                  | 91.5 ms: 1.05x faster                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                       |
| xml_etree_iterparse     | 62.5 ms                                                                  | 61.3 ms: 1.02x faster                                       |
| comprehensions          | 16.0 us                                                                  | 15.7 us: 1.02x faster                                       |
| unpickle                | 8.88 us                                                                  | 8.73 us: 1.02x faster                                       |
| unpack_sequence         | 39.4 ns                                                                  | 38.7 ns: 1.02x faster                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 54.6 ms: 1.01x slower                                       |
| pidigits                | 145 ms                                                                   | 148 ms: 1.02x slower                                        |
| unpickle_list           | 2.71 us                                                                  | 2.80 us: 1.03x slower                                       |
| meteor_contest          | 74.3 ms                                                                  | 77.0 ms: 1.04x slower                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                       |
| pickle                  | 6.67 us                                                                  | 7.02 us: 1.05x slower                                       |
| logging_format          | 6.53 us                                                                  | 6.89 us: 1.06x slower                                       |
| async_generators        | 214 ms                                                                   | 227 ms: 1.06x slower                                        |
| logging_simple          | 6.12 us                                                                  | 6.52 us: 1.07x slower                                       |
| telco                   | 3.77 ms                                                                  | 4.07 ms: 1.08x slower                                       |
| pickle_dict             | 16.7 us                                                                  | 18.1 us: 1.08x slower                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.46 ms: 1.10x slower                                       |
| pathlib                 | 75.2 ms                                                                  | 83.1 ms: 1.11x slower                                       |
| pickle_list             | 2.57 us                                                                  | 2.85 us: 1.11x slower                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 67.2 ms: 1.14x slower                                       |
| dask                    | 310 ms                                                                   | 360 ms: 1.16x slower                                        |
| coverage                | 37.5 ms                                                                  | 52.3 ms: 1.39x slower                                       |
| Geometric mean          | (ref)                                                                    | 1.16x faster                                                |
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
