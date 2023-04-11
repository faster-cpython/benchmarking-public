
# Results vs. 3.11.0

- fork: python
- ref: 5d7d86f2fdbbfc23325e
- machine: linux-x86_64
- commit hash: 5d7d86f
- commit date: 2023-04-07
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                   |
| chameleon      | 6.52 ms                                                             | 6.47 ms: 1.01x faster                                                  |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                 |
| html5lib       | 64.0 ms                                                             | 61.7 ms: 1.04x faster                                                  |
| tornado_http   | 96.7 ms                                                             | 94.1 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.8 ms: 1.09x faster                                                  |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                   |
| float          | 76.0 ms                                                             | 73.3 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                               | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 134 ms: 1.02x faster                                                   |
| regex_v8       | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                  |
| regex_dna      | 196 ms                                                              | 203 ms: 1.04x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.61 ms: 1.30x faster                                                  |
| unpickle_pure_python | 228 us                                                              | 199 us: 1.15x faster                                                   |
| xml_etree_parse      | 162 ms                                                              | 148 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 99.9 ms: 1.08x faster                                                  |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 286 us: 1.07x faster                                                   |
| unpickle_list        | 4.96 us                                                             | 4.99 us: 1.01x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 55.4 ms: 1.02x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 80.0 ms: 1.05x slower                                                  |
| unpickle             | 13.2 us                                                             | 13.9 us: 1.05x slower                                                  |
| pickle_dict          | 30.9 us                                                             | 33.0 us: 1.07x slower                                                  |
| pickle               | 9.79 us                                                             | 10.8 us: 1.10x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.46 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 48.3 ms: 1.07x faster                                                  |
| django_template | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                                  |
| mako            | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.3 ms: 2.51x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 503 ms: 1.77x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 9.61 ms: 1.30x faster                                                  |
| mypy2                   | 422 ms                                                              | 334 ms: 1.26x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.9 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 199 us: 1.15x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.22 ms: 1.14x faster                                                  |
| unpack_sequence         | 49.5 ns                                                             | 43.6 ns: 1.13x faster                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.22 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.05 ms: 1.10x faster                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.50 ms: 1.10x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 148 ms: 1.10x faster                                                   |
| spectral_norm           | 99.5 ms                                                             | 91.2 ms: 1.09x faster                                                  |
| scimark_fft             | 328 ms                                                              | 301 ms: 1.09x faster                                                   |
| nbody                   | 96.7 ms                                                             | 88.8 ms: 1.09x faster                                                  |
| hexiom                  | 6.48 ms                                                             | 5.99 ms: 1.08x faster                                                  |
| logging_simple          | 6.09 us                                                             | 5.63 us: 1.08x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 99.9 ms: 1.08x faster                                                  |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                                  |
| pickle_pure_python      | 307 us                                                              | 286 us: 1.07x faster                                                   |
| genshi_xml              | 51.8 ms                                                             | 48.3 ms: 1.07x faster                                                  |
| deepcopy_memo           | 36.4 us                                                             | 34.0 us: 1.07x faster                                                  |
| logging_format          | 6.64 us                                                             | 6.23 us: 1.07x faster                                                  |
| nqueens                 | 84.0 ms                                                             | 79.4 ms: 1.06x faster                                                  |
| json                    | 4.86 ms                                                             | 4.60 ms: 1.06x faster                                                  |
| sqlglot_optimize        | 53.4 ms                                                             | 50.6 ms: 1.05x faster                                                  |
| coverage                | 101 ms                                                              | 95.9 ms: 1.05x faster                                                  |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                   |
| sqlglot_normalize       | 108 ms                                                              | 104 ms: 1.05x faster                                                   |
| richards                | 45.7 ms                                                             | 43.8 ms: 1.04x faster                                                  |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                                  |
| raytrace                | 292 ms                                                              | 281 ms: 1.04x faster                                                   |
| deepcopy                | 339 us                                                              | 326 us: 1.04x faster                                                   |
| mdp                     | 2.64 sec                                                            | 2.54 sec: 1.04x faster                                                 |
| html5lib                | 64.0 ms                                                             | 61.7 ms: 1.04x faster                                                  |
| bench_thread_pool       | 820 us                                                              | 790 us: 1.04x faster                                                   |
| sympy_expand            | 477 ms                                                              | 459 ms: 1.04x faster                                                   |
| meteor_contest          | 106 ms                                                              | 102 ms: 1.04x faster                                                   |
| float                   | 76.0 ms                                                             | 73.3 ms: 1.04x faster                                                  |
| scimark_lu              | 108 ms                                                              | 105 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                  |
| sympy_str               | 291 ms                                                              | 283 ms: 1.03x faster                                                   |
| async_tree_none         | 525 ms                                                              | 510 ms: 1.03x faster                                                   |
| tornado_http            | 96.7 ms                                                             | 94.1 ms: 1.03x faster                                                  |
| chaos                   | 68.0 ms                                                             | 66.2 ms: 1.03x faster                                                  |
| gunicorn                | 1.13 ms                                                             | 1.10 ms: 1.03x faster                                                  |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                   |
| logging_silent          | 98.7 ns                                                             | 96.5 ns: 1.02x faster                                                  |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                              | 719 ms: 1.02x faster                                                   |
| pprint_pformat          | 1.45 sec                                                            | 1.42 sec: 1.02x faster                                                 |
| comprehensions          | 22.2 us                                                             | 21.8 us: 1.02x faster                                                  |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.5 ms: 1.02x faster                                                  |
| regex_compile           | 137 ms                                                              | 134 ms: 1.02x faster                                                   |
| fannkuch                | 384 ms                                                              | 377 ms: 1.02x faster                                                   |
| sympy_sum               | 167 ms                                                              | 165 ms: 1.02x faster                                                   |
| pprint_safe_repr        | 701 ms                                                              | 692 ms: 1.01x faster                                                   |
| telco                   | 6.59 ms                                                             | 6.51 ms: 1.01x faster                                                  |
| dulwich_log             | 63.6 ms                                                             | 63.0 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                  |
| chameleon               | 6.52 ms                                                             | 6.47 ms: 1.01x faster                                                  |
| django_template         | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                                  |
| crypto_pyaes            | 73.8 ms                                                             | 73.3 ms: 1.01x faster                                                  |
| unpickle_list           | 4.96 us                                                             | 4.99 us: 1.01x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 2.99 us: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                  |
| xml_etree_process       | 54.1 ms                                                             | 55.4 ms: 1.02x slower                                                  |
| thrift                  | 766 us                                                              | 784 us: 1.02x slower                                                   |
| mako                    | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                                  |
| regex_dna               | 196 ms                                                              | 203 ms: 1.04x slower                                                   |
| regex_effbot            | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                                  |
| python_startup          | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.62 us: 1.04x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 80.0 ms: 1.05x slower                                                  |
| unpickle                | 13.2 us                                                             | 13.9 us: 1.05x slower                                                  |
| pickle_dict             | 30.9 us                                                             | 33.0 us: 1.07x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.8 us: 1.10x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.46 us: 1.11x slower                                                  |
| gc_traversal            | 3.63 ms                                                             | 4.07 ms: 1.12x slower                                                  |
| async_generators        | 361 ms                                                              | 415 ms: 1.15x slower                                                   |
| dask                    | 368 ms                                                              | 500 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                           |

Benchmark hidden because not significant (11): sqlalchemy_declarative, genshi_text, pathlib, async_tree_io, async_tree_memoization, bench_mp_pool, pyflate, go, sqlalchemy_imperative, pycparser, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
