
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 244 ms: 1.05x faster                                                   |
| chameleon      | 6.52 ms                                                             | 6.31 ms: 1.03x faster                                                  |
| docutils       | 2.59 sec                                                            | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 64.0 ms                                                             | 59.1 ms: 1.08x faster                                                  |
| tornado_http   | 96.7 ms                                                             | 92.8 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| float          | 76.0 ms                                                             | 73.1 ms: 1.04x faster                                                  |
| nbody          | 96.7 ms                                                             | 93.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                               | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 127 ms: 1.07x faster                                                   |
| regex_v8       | 22.0 ms                                                             | 21.0 ms: 1.04x faster                                                  |
| regex_dna      | 196 ms                                                              | 209 ms: 1.07x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.55 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.51 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                              | 198 us: 1.15x faster                                                   |
| xml_etree_parse      | 162 ms                                                              | 147 ms: 1.10x faster                                                   |
| json_loads           | 26.2 us                                                             | 23.8 us: 1.10x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 281 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 102 ms: 1.06x faster                                                   |
| xml_etree_process    | 54.1 ms                                                             | 52.8 ms: 1.03x faster                                                  |
| pickle_list          | 4.03 us                                                             | 3.97 us: 1.02x faster                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 76.3 ms: 1.00x faster                                                  |
| pickle_dict          | 30.9 us                                                             | 31.3 us: 1.01x slower                                                  |
| unpickle             | 13.2 us                                                             | 13.6 us: 1.03x slower                                                  |
| unpickle_list        | 4.96 us                                                             | 5.13 us: 1.03x slower                                                  |
| pickle               | 9.79 us                                                             | 10.4 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.48 ms: 1.00x faster                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.12 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 46.6 ms: 1.11x faster                                                  |
| genshi_text     | 21.8 ms                                                             | 20.2 ms: 1.08x faster                                                  |
| mako            | 9.82 ms                                                             | 9.56 ms: 1.03x faster                                                  |
| django_template | 32.9 ms                                                             | 32.1 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.5 ms                                                             | 9.51 ms: 1.32x faster                                                  |
| deltablue               | 3.66 ms                                                             | 3.17 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 198 us: 1.15x faster                                                   |
| genshi_xml              | 51.8 ms                                                             | 46.6 ms: 1.11x faster                                                  |
| richards                | 45.7 ms                                                             | 41.3 ms: 1.11x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 147 ms: 1.10x faster                                                   |
| json_loads              | 26.2 us                                                             | 23.8 us: 1.10x faster                                                  |
| unpack_sequence         | 49.5 ns                                                             | 45.1 ns: 1.10x faster                                                  |
| pickle_pure_python      | 307 us                                                              | 281 us: 1.09x faster                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.08 ms: 1.09x faster                                                  |
| logging_simple          | 6.09 us                                                             | 5.62 us: 1.08x faster                                                  |
| html5lib                | 64.0 ms                                                             | 59.1 ms: 1.08x faster                                                  |
| genshi_text             | 21.8 ms                                                             | 20.2 ms: 1.08x faster                                                  |
| deepcopy_memo           | 36.4 us                                                             | 33.8 us: 1.08x faster                                                  |
| scimark_sor             | 115 ms                                                              | 107 ms: 1.08x faster                                                   |
| coroutines              | 26.3 ms                                                             | 24.5 ms: 1.07x faster                                                  |
| regex_compile           | 137 ms                                                              | 127 ms: 1.07x faster                                                   |
| pycparser               | 1.14 sec                                                            | 1.07 sec: 1.07x faster                                                 |
| scimark_fft             | 328 ms                                                              | 307 ms: 1.07x faster                                                   |
| aiohttp                 | 1.05 ms                                                             | 991 us: 1.06x faster                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 50.2 ms: 1.06x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 102 ms: 1.06x faster                                                   |
| gunicorn                | 1.13 ms                                                             | 1.07 ms: 1.06x faster                                                  |
| bench_thread_pool       | 820 us                                                              | 774 us: 1.06x faster                                                   |
| logging_format          | 6.64 us                                                             | 6.29 us: 1.06x faster                                                  |
| json                    | 4.86 ms                                                             | 4.61 ms: 1.05x faster                                                  |
| 2to3                    | 257 ms                                                              | 244 ms: 1.05x faster                                                   |
| sympy_expand            | 477 ms                                                              | 454 ms: 1.05x faster                                                   |
| logging_silent          | 98.7 ns                                                             | 94.1 ns: 1.05x faster                                                  |
| hexiom                  | 6.48 ms                                                             | 6.18 ms: 1.05x faster                                                  |
| sqlglot_normalize       | 108 ms                                                              | 104 ms: 1.05x faster                                                   |
| docutils                | 2.59 sec                                                            | 2.48 sec: 1.05x faster                                                 |
| pprint_pformat          | 1.45 sec                                                            | 1.39 sec: 1.05x faster                                                 |
| regex_v8                | 22.0 ms                                                             | 21.0 ms: 1.04x faster                                                  |
| raytrace                | 292 ms                                                              | 280 ms: 1.04x faster                                                   |
| scimark_monte_carlo     | 67.8 ms                                                             | 65.0 ms: 1.04x faster                                                  |
| tornado_http            | 96.7 ms                                                             | 92.8 ms: 1.04x faster                                                  |
| pyflate                 | 414 ms                                                              | 397 ms: 1.04x faster                                                   |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| spectral_norm           | 99.5 ms                                                             | 95.6 ms: 1.04x faster                                                  |
| meteor_contest          | 106 ms                                                              | 102 ms: 1.04x faster                                                   |
| sympy_str               | 291 ms                                                              | 280 ms: 1.04x faster                                                   |
| float                   | 76.0 ms                                                             | 73.1 ms: 1.04x faster                                                  |
| go                      | 138 ms                                                              | 133 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 701 ms                                                              | 676 ms: 1.04x faster                                                   |
| sympy_integrate         | 21.0 ms                                                             | 20.3 ms: 1.04x faster                                                  |
| chaos                   | 68.0 ms                                                             | 65.6 ms: 1.04x faster                                                  |
| dulwich_log             | 63.6 ms                                                             | 61.5 ms: 1.03x faster                                                  |
| chameleon               | 6.52 ms                                                             | 6.31 ms: 1.03x faster                                                  |
| nbody                   | 96.7 ms                                                             | 93.7 ms: 1.03x faster                                                  |
| fannkuch                | 384 ms                                                              | 373 ms: 1.03x faster                                                   |
| sympy_sum               | 167 ms                                                              | 163 ms: 1.03x faster                                                   |
| sqlglot_parse           | 1.36 ms                                                             | 1.32 ms: 1.03x faster                                                  |
| mako                    | 9.82 ms                                                             | 9.56 ms: 1.03x faster                                                  |
| deepcopy                | 339 us                                                              | 330 us: 1.03x faster                                                   |
| sqlglot_transpile       | 1.65 ms                                                             | 1.61 ms: 1.03x faster                                                  |
| xml_etree_process       | 54.1 ms                                                             | 52.8 ms: 1.03x faster                                                  |
| django_template         | 32.9 ms                                                             | 32.1 ms: 1.02x faster                                                  |
| thrift                  | 766 us                                                              | 748 us: 1.02x faster                                                   |
| nqueens                 | 84.0 ms                                                             | 82.0 ms: 1.02x faster                                                  |
| pathlib                 | 18.2 ms                                                             | 17.8 ms: 1.02x faster                                                  |
| telco                   | 6.59 ms                                                             | 6.44 ms: 1.02x faster                                                  |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                                   |
| pickle_list             | 4.03 us                                                             | 3.97 us: 1.02x faster                                                  |
| async_generators        | 361 ms                                                              | 358 ms: 1.01x faster                                                   |
| xml_etree_generate      | 76.5 ms                                                             | 76.3 ms: 1.00x faster                                                  |
| python_startup          | 8.49 ms                                                             | 8.48 ms: 1.00x faster                                                  |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                   |
| deepcopy_reduce         | 2.96 us                                                             | 2.99 us: 1.01x slower                                                  |
| pickle_dict             | 30.9 us                                                             | 31.3 us: 1.01x slower                                                  |
| crypto_pyaes            | 73.8 ms                                                             | 75.1 ms: 1.02x slower                                                  |
| mdp                     | 2.64 sec                                                            | 2.69 sec: 1.02x slower                                                 |
| python_startup_no_site  | 5.98 ms                                                             | 6.12 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 755 ms: 1.03x slower                                                   |
| unpickle                | 13.2 us                                                             | 13.6 us: 1.03x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.59 us: 1.03x slower                                                  |
| async_tree_io           | 1.28 sec                                                            | 1.32 sec: 1.03x slower                                                 |
| unpickle_list           | 4.96 us                                                             | 5.13 us: 1.03x slower                                                  |
| generators              | 73.4 ms                                                             | 77.7 ms: 1.06x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.4 us: 1.06x slower                                                  |
| regex_dna               | 196 ms                                                              | 209 ms: 1.07x slower                                                   |
| regex_effbot            | 3.32 ms                                                             | 3.55 ms: 1.07x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                           |

Benchmark hidden because not significant (3): bench_mp_pool, async_tree_memoization, async_tree_none
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy
