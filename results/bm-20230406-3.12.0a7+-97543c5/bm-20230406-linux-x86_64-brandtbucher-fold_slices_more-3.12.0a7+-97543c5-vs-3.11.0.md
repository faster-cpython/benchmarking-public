
# Results vs. 3.11.0

- fork: brandtbucher
- ref: fold_slices_more
- machine: linux-x86_64
- commit hash: 97543c5
- commit date: 2023-04-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 250 ms: 1.03x faster                                                     |
| chameleon      | 6.52 ms                                                             | 6.41 ms: 1.02x faster                                                    |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                   |
| html5lib       | 64.0 ms                                                             | 61.0 ms: 1.05x faster                                                    |
| tornado_http   | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                               | 1.04x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 86.9 ms: 1.11x faster                                                    |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                     |
| float          | 76.0 ms                                                             | 74.7 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                               | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 132 ms: 1.03x faster                                                     |
| regex_v8       | 22.0 ms                                                             | 21.6 ms: 1.01x faster                                                    |
| regex_effbot   | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                    |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                               | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.37 ms: 1.34x faster                                                    |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                     |
| xml_etree_parse      | 162 ms                                                              | 147 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 108 ms                                                              | 99.4 ms: 1.08x faster                                                    |
| json_loads           | 26.2 us                                                             | 24.2 us: 1.08x faster                                                    |
| pickle_pure_python   | 307 us                                                              | 287 us: 1.07x faster                                                     |
| unpickle_list        | 4.96 us                                                             | 5.05 us: 1.02x slower                                                    |
| xml_etree_process    | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                                    |
| pickle_dict          | 30.9 us                                                             | 31.9 us: 1.03x slower                                                    |
| unpickle             | 13.2 us                                                             | 13.8 us: 1.05x slower                                                    |
| xml_etree_generate   | 76.5 ms                                                             | 80.6 ms: 1.05x slower                                                    |
| pickle               | 9.79 us                                                             | 10.6 us: 1.08x slower                                                    |
| pickle_list          | 4.03 us                                                             | 4.43 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.82 ms: 1.04x slower                                                    |
| python_startup_no_site | 5.98 ms                                                             | 6.52 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 46.9 ms: 1.10x faster                                                    |
| genshi_text     | 21.8 ms                                                             | 21.1 ms: 1.03x faster                                                    |
| django_template | 32.9 ms                                                             | 32.4 ms: 1.01x faster                                                    |
| mako            | 9.82 ms                                                             | 10.1 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.9 ms: 2.46x faster                                                    |
| asyncio_tcp             | 888 ms                                                              | 500 ms: 1.78x faster                                                     |
| json_dumps              | 12.5 ms                                                             | 9.37 ms: 1.34x faster                                                    |
| mypy2                   | 422 ms                                                              | 334 ms: 1.26x faster                                                     |
| unpack_sequence         | 49.5 ns                                                             | 43.5 ns: 1.14x faster                                                    |
| deltablue               | 3.66 ms                                                             | 3.24 ms: 1.13x faster                                                    |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                     |
| nbody                   | 96.7 ms                                                             | 86.9 ms: 1.11x faster                                                    |
| sqlglot_parse           | 1.36 ms                                                             | 1.22 ms: 1.11x faster                                                    |
| coroutines              | 26.3 ms                                                             | 23.7 ms: 1.11x faster                                                    |
| genshi_xml              | 51.8 ms                                                             | 46.9 ms: 1.10x faster                                                    |
| richards                | 45.7 ms                                                             | 41.4 ms: 1.10x faster                                                    |
| sqlglot_transpile       | 1.65 ms                                                             | 1.50 ms: 1.10x faster                                                    |
| xml_etree_parse         | 162 ms                                                              | 147 ms: 1.10x faster                                                     |
| hexiom                  | 6.48 ms                                                             | 5.92 ms: 1.10x faster                                                    |
| xml_etree_iterparse     | 108 ms                                                              | 99.4 ms: 1.08x faster                                                    |
| json_loads              | 26.2 us                                                             | 24.2 us: 1.08x faster                                                    |
| pickle_pure_python      | 307 us                                                              | 287 us: 1.07x faster                                                     |
| tornado_http            | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                                    |
| logging_simple          | 6.09 us                                                             | 5.71 us: 1.07x faster                                                    |
| deepcopy_memo           | 36.4 us                                                             | 34.3 us: 1.06x faster                                                    |
| sqlglot_optimize        | 53.4 ms                                                             | 50.4 ms: 1.06x faster                                                    |
| logging_format          | 6.64 us                                                             | 6.30 us: 1.05x faster                                                    |
| json                    | 4.86 ms                                                             | 4.63 ms: 1.05x faster                                                    |
| coverage                | 101 ms                                                              | 96.3 ms: 1.05x faster                                                    |
| html5lib                | 64.0 ms                                                             | 61.0 ms: 1.05x faster                                                    |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.27 ms: 1.05x faster                                                    |
| spectral_norm           | 99.5 ms                                                             | 95.1 ms: 1.05x faster                                                    |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                    |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                     |
| scimark_fft             | 328 ms                                                              | 314 ms: 1.04x faster                                                     |
| sqlglot_normalize       | 108 ms                                                              | 104 ms: 1.04x faster                                                     |
| mdp                     | 2.64 sec                                                            | 2.53 sec: 1.04x faster                                                   |
| logging_silent          | 98.7 ns                                                             | 95.0 ns: 1.04x faster                                                    |
| deepcopy                | 339 us                                                              | 326 us: 1.04x faster                                                     |
| chaos                   | 68.0 ms                                                             | 65.4 ms: 1.04x faster                                                    |
| bench_thread_pool       | 820 us                                                              | 791 us: 1.04x faster                                                     |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.04x faster                                                    |
| sympy_expand            | 477 ms                                                              | 460 ms: 1.04x faster                                                     |
| meteor_contest          | 106 ms                                                              | 103 ms: 1.04x faster                                                     |
| regex_compile           | 137 ms                                                              | 132 ms: 1.03x faster                                                     |
| genshi_text             | 21.8 ms                                                             | 21.1 ms: 1.03x faster                                                    |
| raytrace                | 292 ms                                                              | 283 ms: 1.03x faster                                                     |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                    |
| sympy_str               | 291 ms                                                              | 284 ms: 1.03x faster                                                     |
| 2to3                    | 257 ms                                                              | 250 ms: 1.03x faster                                                     |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.6 ms: 1.03x faster                                                    |
| pprint_pformat          | 1.45 sec                                                            | 1.42 sec: 1.02x faster                                                   |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                     |
| scimark_sor             | 115 ms                                                              | 113 ms: 1.02x faster                                                     |
| telco                   | 6.59 ms                                                             | 6.47 ms: 1.02x faster                                                    |
| float                   | 76.0 ms                                                             | 74.7 ms: 1.02x faster                                                    |
| nqueens                 | 84.0 ms                                                             | 82.6 ms: 1.02x faster                                                    |
| chameleon               | 6.52 ms                                                             | 6.41 ms: 1.02x faster                                                    |
| regex_v8                | 22.0 ms                                                             | 21.6 ms: 1.01x faster                                                    |
| comprehensions          | 22.2 us                                                             | 21.9 us: 1.01x faster                                                    |
| django_template         | 32.9 ms                                                             | 32.4 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.96 us                                                             | 2.92 us: 1.01x faster                                                    |
| sympy_sum               | 167 ms                                                              | 165 ms: 1.01x faster                                                     |
| pprint_safe_repr        | 701 ms                                                              | 694 ms: 1.01x faster                                                     |
| dulwich_log             | 63.6 ms                                                             | 63.1 ms: 1.01x faster                                                    |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                                    |
| unpickle_list           | 4.96 us                                                             | 5.05 us: 1.02x slower                                                    |
| thrift                  | 766 us                                                              | 782 us: 1.02x slower                                                     |
| xml_etree_process       | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                                    |
| mako                    | 9.82 ms                                                             | 10.1 ms: 1.02x slower                                                    |
| regex_effbot            | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                    |
| pyflate                 | 414 ms                                                              | 425 ms: 1.03x slower                                                     |
| pickle_dict             | 30.9 us                                                             | 31.9 us: 1.03x slower                                                    |
| create_gc_cycles        | 1.48 ms                                                             | 1.52 ms: 1.03x slower                                                    |
| python_startup          | 8.49 ms                                                             | 8.82 ms: 1.04x slower                                                    |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                     |
| unpickle                | 13.2 us                                                             | 13.8 us: 1.05x slower                                                    |
| sqlite_synth            | 2.51 us                                                             | 2.64 us: 1.05x slower                                                    |
| xml_etree_generate      | 76.5 ms                                                             | 80.6 ms: 1.05x slower                                                    |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.08x slower                                                    |
| python_startup_no_site  | 5.98 ms                                                             | 6.52 ms: 1.09x slower                                                    |
| gc_traversal            | 3.63 ms                                                             | 3.97 ms: 1.09x slower                                                    |
| pickle_list             | 4.03 us                                                             | 4.43 us: 1.10x slower                                                    |
| async_generators        | 361 ms                                                              | 413 ms: 1.14x slower                                                     |
| dask                    | 368 ms                                                              | 503 ms: 1.37x slower                                                     |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                             |

Benchmark hidden because not significant (12): djangocms, async_tree_none, async_tree_cpu_io_mixed, go, fannkuch, bench_mp_pool, pycparser, crypto_pyaes, async_tree_memoization, scimark_lu, scimark_monte_carlo, async_tree_io
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
