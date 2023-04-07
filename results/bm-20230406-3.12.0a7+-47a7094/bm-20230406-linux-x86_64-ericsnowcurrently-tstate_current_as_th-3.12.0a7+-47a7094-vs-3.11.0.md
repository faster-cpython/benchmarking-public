
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: linux-x86_64
- commit hash: 47a7094
- commit date: 2023-04-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                              |
| chameleon      | 6.52 ms                                                             | 6.42 ms: 1.01x faster                                                             |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                            |
| html5lib       | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                                             |
| tornado_http   | 96.7 ms                                                             | 90.3 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                               | 1.04x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 83.6 ms: 1.16x faster                                                             |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| float          | 76.0 ms                                                             | 72.6 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 132 ms: 1.03x faster                                                              |
| regex_v8       | 22.0 ms                                                             | 22.6 ms: 1.03x slower                                                             |
| regex_dna      | 196 ms                                                              | 214 ms: 1.09x slower                                                              |
| regex_effbot   | 3.32 ms                                                             | 3.63 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.46 ms: 1.33x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 201 us: 1.14x faster                                                              |
| xml_etree_parse      | 162 ms                                                              | 147 ms: 1.10x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 99.4 ms: 1.08x faster                                                             |
| json_loads           | 26.2 us                                                             | 24.5 us: 1.07x faster                                                             |
| pickle_pure_python   | 307 us                                                              | 292 us: 1.05x faster                                                              |
| unpickle_list        | 4.96 us                                                             | 4.87 us: 1.02x faster                                                             |
| xml_etree_process    | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                                             |
| unpickle             | 13.2 us                                                             | 13.6 us: 1.03x slower                                                             |
| pickle_dict          | 30.9 us                                                             | 32.3 us: 1.04x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 80.7 ms: 1.05x slower                                                             |
| pickle               | 9.79 us                                                             | 10.6 us: 1.08x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.43 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.87 ms: 1.04x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.55 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.3 ms: 1.09x faster                                                             |
| genshi_text     | 21.8 ms                                                             | 21.1 ms: 1.04x faster                                                             |
| django_template | 32.9 ms                                                             | 32.0 ms: 1.03x faster                                                             |
| mako            | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.4 ms: 2.50x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 501 ms: 1.77x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 9.46 ms: 1.33x faster                                                             |
| mypy2                   | 422 ms                                                              | 333 ms: 1.27x faster                                                              |
| unpack_sequence         | 49.5 ns                                                             | 42.1 ns: 1.18x faster                                                             |
| nbody                   | 96.7 ms                                                             | 83.6 ms: 1.16x faster                                                             |
| coroutines              | 26.3 ms                                                             | 22.9 ms: 1.14x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.20 ms: 1.14x faster                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.20 ms: 1.14x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 201 us: 1.14x faster                                                              |
| sqlglot_transpile       | 1.65 ms                                                             | 1.48 ms: 1.12x faster                                                             |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.01 ms: 1.11x faster                                                             |
| xml_etree_parse         | 162 ms                                                              | 147 ms: 1.10x faster                                                              |
| genshi_xml              | 51.8 ms                                                             | 47.3 ms: 1.09x faster                                                             |
| xml_etree_iterparse     | 108 ms                                                              | 99.4 ms: 1.08x faster                                                             |
| deepcopy_memo           | 36.4 us                                                             | 33.6 us: 1.08x faster                                                             |
| scimark_fft             | 328 ms                                                              | 306 ms: 1.07x faster                                                              |
| hexiom                  | 6.48 ms                                                             | 6.05 ms: 1.07x faster                                                             |
| logging_simple          | 6.09 us                                                             | 5.69 us: 1.07x faster                                                             |
| tornado_http            | 96.7 ms                                                             | 90.3 ms: 1.07x faster                                                             |
| json_loads              | 26.2 us                                                             | 24.5 us: 1.07x faster                                                             |
| spectral_norm           | 99.5 ms                                                             | 93.2 ms: 1.07x faster                                                             |
| sqlglot_normalize       | 108 ms                                                              | 102 ms: 1.06x faster                                                              |
| raytrace                | 292 ms                                                              | 275 ms: 1.06x faster                                                              |
| sqlglot_optimize        | 53.4 ms                                                             | 50.3 ms: 1.06x faster                                                             |
| richards                | 45.7 ms                                                             | 43.1 ms: 1.06x faster                                                             |
| nqueens                 | 84.0 ms                                                             | 79.4 ms: 1.06x faster                                                             |
| logging_silent          | 98.7 ns                                                             | 93.5 ns: 1.06x faster                                                             |
| logging_format          | 6.64 us                                                             | 6.31 us: 1.05x faster                                                             |
| pickle_pure_python      | 307 us                                                              | 292 us: 1.05x faster                                                              |
| chaos                   | 68.0 ms                                                             | 64.7 ms: 1.05x faster                                                             |
| scimark_sor             | 115 ms                                                              | 109 ms: 1.05x faster                                                              |
| pprint_pformat          | 1.45 sec                                                            | 1.39 sec: 1.05x faster                                                            |
| coverage                | 101 ms                                                              | 96.6 ms: 1.05x faster                                                             |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| meteor_contest          | 106 ms                                                              | 101 ms: 1.05x faster                                                              |
| float                   | 76.0 ms                                                             | 72.6 ms: 1.05x faster                                                             |
| deepcopy                | 339 us                                                              | 324 us: 1.05x faster                                                              |
| html5lib                | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                                             |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                                             |
| pprint_safe_repr        | 701 ms                                                              | 671 ms: 1.04x faster                                                              |
| sympy_expand            | 477 ms                                                              | 457 ms: 1.04x faster                                                              |
| bench_thread_pool       | 820 us                                                              | 788 us: 1.04x faster                                                              |
| comprehensions          | 22.2 us                                                             | 21.4 us: 1.04x faster                                                             |
| genshi_text             | 21.8 ms                                                             | 21.1 ms: 1.04x faster                                                             |
| sympy_str               | 291 ms                                                              | 282 ms: 1.03x faster                                                              |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                             |
| regex_compile           | 137 ms                                                              | 132 ms: 1.03x faster                                                              |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.03x faster                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 65.7 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 715 ms: 1.03x faster                                                              |
| django_template         | 32.9 ms                                                             | 32.0 ms: 1.03x faster                                                             |
| json                    | 4.86 ms                                                             | 4.73 ms: 1.03x faster                                                             |
| async_tree_memoization  | 621 ms                                                              | 605 ms: 1.03x faster                                                              |
| async_tree_none         | 525 ms                                                              | 512 ms: 1.03x faster                                                              |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.6 ms: 1.03x faster                                                             |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                            |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                                              |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                              |
| go                      | 138 ms                                                              | 135 ms: 1.02x faster                                                              |
| fannkuch                | 384 ms                                                              | 377 ms: 1.02x faster                                                              |
| unpickle_list           | 4.96 us                                                             | 4.87 us: 1.02x faster                                                             |
| telco                   | 6.59 ms                                                             | 6.48 ms: 1.02x faster                                                             |
| chameleon               | 6.52 ms                                                             | 6.42 ms: 1.01x faster                                                             |
| sympy_sum               | 167 ms                                                              | 165 ms: 1.01x faster                                                              |
| dulwich_log             | 63.6 ms                                                             | 62.8 ms: 1.01x faster                                                             |
| async_tree_io           | 1.28 sec                                                            | 1.27 sec: 1.01x faster                                                            |
| deepcopy_reduce         | 2.96 us                                                             | 2.94 us: 1.01x faster                                                             |
| pyflate                 | 414 ms                                                              | 416 ms: 1.01x slower                                                              |
| crypto_pyaes            | 73.8 ms                                                             | 74.4 ms: 1.01x slower                                                             |
| mako                    | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                                             |
| mdp                     | 2.64 sec                                                            | 2.68 sec: 1.02x slower                                                            |
| unpickle                | 13.2 us                                                             | 13.6 us: 1.03x slower                                                             |
| thrift                  | 766 us                                                              | 787 us: 1.03x slower                                                              |
| regex_v8                | 22.0 ms                                                             | 22.6 ms: 1.03x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 32.3 us: 1.04x slower                                                             |
| python_startup          | 8.49 ms                                                             | 8.87 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.63 us: 1.05x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 80.7 ms: 1.05x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.08x slower                                                             |
| regex_dna               | 196 ms                                                              | 214 ms: 1.09x slower                                                              |
| regex_effbot            | 3.32 ms                                                             | 3.63 ms: 1.09x slower                                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.55 ms: 1.10x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.43 us: 1.10x slower                                                             |
| async_generators        | 361 ms                                                              | 409 ms: 1.13x slower                                                              |
| gc_traversal            | 3.63 ms                                                             | 4.19 ms: 1.16x slower                                                             |
| dask                    | 368 ms                                                              | 499 ms: 1.35x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                                      |

Benchmark hidden because not significant (6): pycparser, djangocms, create_gc_cycles, bench_mp_pool, sqlalchemy_declarative, pathlib
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
