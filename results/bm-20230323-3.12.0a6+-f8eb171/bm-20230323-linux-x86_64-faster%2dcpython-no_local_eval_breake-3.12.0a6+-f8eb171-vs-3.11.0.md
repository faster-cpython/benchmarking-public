
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 254 ms: 1.01x faster                                                             |
| chameleon      | 6.52 ms                                                             | 6.44 ms: 1.01x faster                                                            |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                           |
| html5lib       | 64.0 ms                                                             | 62.5 ms: 1.02x faster                                                            |
| tornado_http   | 96.7 ms                                                             | 91.1 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.6 ms: 1.10x faster                                                            |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                             |
| float          | 76.0 ms                                                             | 75.2 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                               | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                                             |
| regex_v8       | 22.0 ms                                                             | 21.9 ms: 1.00x faster                                                            |
| regex_effbot   | 3.32 ms                                                             | 3.50 ms: 1.05x slower                                                            |
| regex_dna      | 196 ms                                                              | 207 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.61 ms: 1.30x faster                                                            |
| unpickle_pure_python | 228 us                                                              | 203 us: 1.12x faster                                                             |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                                             |
| json_loads           | 26.2 us                                                             | 24.1 us: 1.09x faster                                                            |
| xml_etree_iterparse  | 108 ms                                                              | 100 ms: 1.08x faster                                                             |
| pickle_pure_python   | 307 us                                                              | 288 us: 1.07x faster                                                             |
| pickle_dict          | 30.9 us                                                             | 31.1 us: 1.01x slower                                                            |
| unpickle_list        | 4.96 us                                                             | 5.00 us: 1.01x slower                                                            |
| unpickle             | 13.2 us                                                             | 13.6 us: 1.03x slower                                                            |
| pickle_list          | 4.03 us                                                             | 4.21 us: 1.04x slower                                                            |
| xml_etree_process    | 54.1 ms                                                             | 56.5 ms: 1.04x slower                                                            |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                                            |
| xml_etree_generate   | 76.5 ms                                                             | 81.8 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                                            |
| python_startup_no_site | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 48.2 ms: 1.07x faster                                                            |
| genshi_text     | 21.8 ms                                                             | 21.6 ms: 1.01x faster                                                            |
| mako            | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                            |
| django_template | 32.9 ms                                                             | 33.6 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.3 ms: 2.51x faster                                                            |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.75x faster                                                             |
| json_dumps              | 12.5 ms                                                             | 9.61 ms: 1.30x faster                                                            |
| mypy2                   | 422 ms                                                              | 334 ms: 1.26x faster                                                             |
| coroutines              | 26.3 ms                                                             | 23.1 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 228 us                                                              | 203 us: 1.12x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.26 ms: 1.12x faster                                                            |
| nbody                   | 96.7 ms                                                             | 87.6 ms: 1.10x faster                                                            |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                                             |
| json_loads              | 26.2 us                                                             | 24.1 us: 1.09x faster                                                            |
| spectral_norm           | 99.5 ms                                                             | 92.1 ms: 1.08x faster                                                            |
| xml_etree_iterparse     | 108 ms                                                              | 100 ms: 1.08x faster                                                             |
| genshi_xml              | 51.8 ms                                                             | 48.2 ms: 1.07x faster                                                            |
| scimark_fft             | 328 ms                                                              | 307 ms: 1.07x faster                                                             |
| logging_simple          | 6.09 us                                                             | 5.71 us: 1.07x faster                                                            |
| pickle_pure_python      | 307 us                                                              | 288 us: 1.07x faster                                                             |
| unpack_sequence         | 49.5 ns                                                             | 46.5 ns: 1.06x faster                                                            |
| tornado_http            | 96.7 ms                                                             | 91.1 ms: 1.06x faster                                                            |
| hexiom                  | 6.48 ms                                                             | 6.14 ms: 1.06x faster                                                            |
| logging_format          | 6.64 us                                                             | 6.30 us: 1.05x faster                                                            |
| json                    | 4.86 ms                                                             | 4.63 ms: 1.05x faster                                                            |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.52 sec: 1.05x faster                                                           |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                            |
| deepcopy_memo           | 36.4 us                                                             | 34.8 us: 1.05x faster                                                            |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.28 ms: 1.04x faster                                                            |
| nqueens                 | 84.0 ms                                                             | 80.6 ms: 1.04x faster                                                            |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.04x faster                                                            |
| coverage                | 101 ms                                                              | 97.5 ms: 1.04x faster                                                            |
| bench_thread_pool       | 820 us                                                              | 791 us: 1.04x faster                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 51.5 ms: 1.04x faster                                                            |
| sympy_expand            | 477 ms                                                              | 460 ms: 1.04x faster                                                             |
| fannkuch                | 384 ms                                                              | 370 ms: 1.04x faster                                                             |
| pprint_pformat          | 1.45 sec                                                            | 1.40 sec: 1.03x faster                                                           |
| telco                   | 6.59 ms                                                             | 6.39 ms: 1.03x faster                                                            |
| chaos                   | 68.0 ms                                                             | 66.1 ms: 1.03x faster                                                            |
| pprint_safe_repr        | 701 ms                                                              | 683 ms: 1.03x faster                                                             |
| raytrace                | 292 ms                                                              | 285 ms: 1.02x faster                                                             |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.02x faster                                                            |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.02x faster                                                             |
| sympy_str               | 291 ms                                                              | 285 ms: 1.02x faster                                                             |
| html5lib                | 64.0 ms                                                             | 62.5 ms: 1.02x faster                                                            |
| richards                | 45.7 ms                                                             | 44.7 ms: 1.02x faster                                                            |
| pycparser               | 1.14 sec                                                            | 1.12 sec: 1.02x faster                                                           |
| sqlglot_normalize       | 108 ms                                                              | 106 ms: 1.02x faster                                                             |
| deepcopy                | 339 us                                                              | 333 us: 1.02x faster                                                             |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                           |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.8 ms: 1.01x faster                                                            |
| 2to3                    | 257 ms                                                              | 254 ms: 1.01x faster                                                             |
| chameleon               | 6.52 ms                                                             | 6.44 ms: 1.01x faster                                                            |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                             |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                             |
| float                   | 76.0 ms                                                             | 75.2 ms: 1.01x faster                                                            |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 67.1 ms: 1.01x faster                                                            |
| genshi_text             | 21.8 ms                                                             | 21.6 ms: 1.01x faster                                                            |
| sqlalchemy_declarative  | 138 ms                                                              | 137 ms: 1.01x faster                                                             |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                                            |
| dulwich_log             | 63.6 ms                                                             | 63.3 ms: 1.01x faster                                                            |
| regex_v8                | 22.0 ms                                                             | 21.9 ms: 1.00x faster                                                            |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.00x slower                                                            |
| pickle_dict             | 30.9 us                                                             | 31.1 us: 1.01x slower                                                            |
| unpickle_list           | 4.96 us                                                             | 5.00 us: 1.01x slower                                                            |
| mako                    | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                            |
| crypto_pyaes            | 73.8 ms                                                             | 74.8 ms: 1.01x slower                                                            |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.02x slower                                                           |
| scimark_lu              | 108 ms                                                              | 110 ms: 1.02x slower                                                             |
| deepcopy_reduce         | 2.96 us                                                             | 3.02 us: 1.02x slower                                                            |
| pyflate                 | 414 ms                                                              | 423 ms: 1.02x slower                                                             |
| django_template         | 32.9 ms                                                             | 33.6 ms: 1.02x slower                                                            |
| thrift                  | 766 us                                                              | 786 us: 1.03x slower                                                             |
| unpickle                | 13.2 us                                                             | 13.6 us: 1.03x slower                                                            |
| sqlite_synth            | 2.51 us                                                             | 2.61 us: 1.04x slower                                                            |
| python_startup          | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                             | 1.72 ms: 1.04x slower                                                            |
| pickle_list             | 4.03 us                                                             | 4.21 us: 1.04x slower                                                            |
| xml_etree_process       | 54.1 ms                                                             | 56.5 ms: 1.04x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                             | 1.43 ms: 1.05x slower                                                            |
| regex_effbot            | 3.32 ms                                                             | 3.50 ms: 1.05x slower                                                            |
| gc_traversal            | 3.63 ms                                                             | 3.82 ms: 1.05x slower                                                            |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                                            |
| async_tree_memoization  | 621 ms                                                              | 656 ms: 1.06x slower                                                             |
| regex_dna               | 196 ms                                                              | 207 ms: 1.06x slower                                                             |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                            |
| xml_etree_generate      | 76.5 ms                                                             | 81.8 ms: 1.07x slower                                                            |
| python_startup_no_site  | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                                            |
| async_generators        | 361 ms                                                              | 407 ms: 1.13x slower                                                             |
| dask                    | 368 ms                                                              | 512 ms: 1.39x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                                     |

Benchmark hidden because not significant (5): logging_silent, async_tree_none, djangocms, bench_mp_pool, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
