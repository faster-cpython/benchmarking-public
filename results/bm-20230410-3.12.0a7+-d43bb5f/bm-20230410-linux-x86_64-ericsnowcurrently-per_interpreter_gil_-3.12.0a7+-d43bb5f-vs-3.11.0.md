
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: d43bb5f
- commit date: 2023-04-10
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 252 ms: 1.02x faster                                                              |
| docutils       | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                                            |
| html5lib       | 64.0 ms                                                             | 62.4 ms: 1.03x faster                                                             |
| tornado_http   | 96.7 ms                                                             | 94.1 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 84.4 ms: 1.15x faster                                                             |
| float          | 76.0 ms                                                             | 74.3 ms: 1.02x faster                                                             |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                               | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 133 ms: 1.03x faster                                                              |
| regex_v8       | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                                             |
| regex_dna      | 196 ms                                                              | 208 ms: 1.06x slower                                                              |
| regex_effbot   | 3.32 ms                                                             | 3.64 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.80 ms: 1.28x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 201 us: 1.13x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 99.7 ms: 1.08x faster                                                             |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                                             |
| xml_etree_parse      | 162 ms                                                              | 151 ms: 1.07x faster                                                              |
| pickle_pure_python   | 307 us                                                              | 289 us: 1.06x faster                                                              |
| unpickle_list        | 4.96 us                                                             | 4.91 us: 1.01x faster                                                             |
| xml_etree_process    | 54.1 ms                                                             | 55.5 ms: 1.03x slower                                                             |
| pickle_dict          | 30.9 us                                                             | 31.9 us: 1.03x slower                                                             |
| unpickle             | 13.2 us                                                             | 13.7 us: 1.04x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 81.2 ms: 1.06x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.35 us: 1.08x slower                                                             |
| pickle               | 9.79 us                                                             | 10.7 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.92 ms: 1.05x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.59 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 48.6 ms: 1.06x faster                                                             |
| genshi_text    | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                                             |
| mako           | 9.82 ms                                                             | 10.2 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.1 ms: 2.44x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 503 ms: 1.77x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 9.80 ms: 1.28x faster                                                             |
| mypy2                   | 422 ms                                                              | 336 ms: 1.26x faster                                                              |
| coroutines              | 26.3 ms                                                             | 22.4 ms: 1.17x faster                                                             |
| nbody                   | 96.7 ms                                                             | 84.4 ms: 1.15x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 201 us: 1.13x faster                                                              |
| deltablue               | 3.66 ms                                                             | 3.23 ms: 1.13x faster                                                             |
| unpack_sequence         | 49.5 ns                                                             | 43.8 ns: 1.13x faster                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.23 ms: 1.11x faster                                                             |
| sqlglot_transpile       | 1.65 ms                                                             | 1.51 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 108 ms                                                              | 99.7 ms: 1.08x faster                                                             |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                                             |
| hexiom                  | 6.48 ms                                                             | 6.04 ms: 1.07x faster                                                             |
| xml_etree_parse         | 162 ms                                                              | 151 ms: 1.07x faster                                                              |
| scimark_fft             | 328 ms                                                              | 308 ms: 1.07x faster                                                              |
| genshi_xml              | 51.8 ms                                                             | 48.6 ms: 1.06x faster                                                             |
| pickle_pure_python      | 307 us                                                              | 289 us: 1.06x faster                                                              |
| richards                | 45.7 ms                                                             | 43.1 ms: 1.06x faster                                                             |
| logging_simple          | 6.09 us                                                             | 5.75 us: 1.06x faster                                                             |
| deepcopy_memo           | 36.4 us                                                             | 34.5 us: 1.06x faster                                                             |
| raytrace                | 292 ms                                                              | 279 ms: 1.05x faster                                                              |
| logging_format          | 6.64 us                                                             | 6.36 us: 1.04x faster                                                             |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 51.1 ms: 1.04x faster                                                             |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.29 ms: 1.04x faster                                                             |
| sqlglot_normalize       | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| meteor_contest          | 106 ms                                                              | 102 ms: 1.04x faster                                                              |
| chaos                   | 68.0 ms                                                             | 65.4 ms: 1.04x faster                                                             |
| coverage                | 101 ms                                                              | 97.4 ms: 1.04x faster                                                             |
| json                    | 4.86 ms                                                             | 4.70 ms: 1.03x faster                                                             |
| sympy_expand            | 477 ms                                                              | 462 ms: 1.03x faster                                                              |
| bench_thread_pool       | 820 us                                                              | 796 us: 1.03x faster                                                              |
| gunicorn                | 1.13 ms                                                             | 1.10 ms: 1.03x faster                                                             |
| tornado_http            | 96.7 ms                                                             | 94.1 ms: 1.03x faster                                                             |
| regex_compile           | 137 ms                                                              | 133 ms: 1.03x faster                                                              |
| telco                   | 6.59 ms                                                             | 6.42 ms: 1.03x faster                                                             |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                                             |
| html5lib                | 64.0 ms                                                             | 62.4 ms: 1.03x faster                                                             |
| sympy_str               | 291 ms                                                              | 284 ms: 1.03x faster                                                              |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.02x faster                                                              |
| float                   | 76.0 ms                                                             | 74.3 ms: 1.02x faster                                                             |
| nqueens                 | 84.0 ms                                                             | 82.1 ms: 1.02x faster                                                             |
| comprehensions          | 22.2 us                                                             | 21.8 us: 1.02x faster                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.4 ms: 1.02x faster                                                             |
| 2to3                    | 257 ms                                                              | 252 ms: 1.02x faster                                                              |
| async_tree_none         | 525 ms                                                              | 516 ms: 1.02x faster                                                              |
| pprint_pformat          | 1.45 sec                                                            | 1.43 sec: 1.02x faster                                                            |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.02x faster                                                              |
| spectral_norm           | 99.5 ms                                                             | 97.8 ms: 1.02x faster                                                             |
| pprint_safe_repr        | 701 ms                                                              | 690 ms: 1.02x faster                                                              |
| logging_silent          | 98.7 ns                                                             | 97.4 ns: 1.01x faster                                                             |
| sqlalchemy_declarative  | 138 ms                                                              | 137 ms: 1.01x faster                                                              |
| deepcopy                | 339 us                                                              | 334 us: 1.01x faster                                                              |
| unpickle_list           | 4.96 us                                                             | 4.91 us: 1.01x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.61 sec: 1.01x faster                                                            |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                              |
| docutils                | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                                            |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                              |
| genshi_text             | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                                             |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x faster                                                              |
| thrift                  | 766 us                                                              | 771 us: 1.01x slower                                                              |
| pathlib                 | 18.2 ms                                                             | 18.3 ms: 1.01x slower                                                             |
| async_tree_io           | 1.28 sec                                                            | 1.29 sec: 1.01x slower                                                            |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                                            |
| deepcopy_reduce         | 2.96 us                                                             | 3.00 us: 1.01x slower                                                             |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.02x slower                                                             |
| crypto_pyaes            | 73.8 ms                                                             | 75.0 ms: 1.02x slower                                                             |
| pyflate                 | 414 ms                                                              | 422 ms: 1.02x slower                                                              |
| regex_v8                | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 55.5 ms: 1.03x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 31.9 us: 1.03x slower                                                             |
| unpickle                | 13.2 us                                                             | 13.7 us: 1.04x slower                                                             |
| mako                    | 9.82 ms                                                             | 10.2 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.64 us: 1.05x slower                                                             |
| python_startup          | 8.49 ms                                                             | 8.92 ms: 1.05x slower                                                             |
| regex_dna               | 196 ms                                                              | 208 ms: 1.06x slower                                                              |
| gc_traversal            | 3.63 ms                                                             | 3.85 ms: 1.06x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 81.2 ms: 1.06x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.35 us: 1.08x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.10x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.64 ms: 1.10x slower                                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.59 ms: 1.10x slower                                                             |
| async_generators        | 361 ms                                                              | 412 ms: 1.14x slower                                                              |
| dask                    | 368 ms                                                              | 504 ms: 1.37x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                                      |

Benchmark hidden because not significant (9): sqlalchemy_imperative, async_tree_cpu_io_mixed, fannkuch, bench_mp_pool, async_tree_memoization, chameleon, dulwich_log, django_template, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
