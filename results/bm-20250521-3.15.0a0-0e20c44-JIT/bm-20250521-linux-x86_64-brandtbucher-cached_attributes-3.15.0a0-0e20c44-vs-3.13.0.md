# Results vs. 3.13.0

- fork: brandtbucher
- ref: cached_attributes
- machine: linux-x86_64
- commit hash: 0e20c44
- commit date: 2025-05-21
- overall geometric mean: 1.029x slower
- HPT reliability: 98.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                   |
| html5lib       | 63.4 ms                                                | 62.9 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                     |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                     |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                     |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.2 ms: 1.22x faster                                                    |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| nbody          | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                    |
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                    |
| regex_dna      | 220 ms                                                 | 203 ms: 1.09x faster                                                     |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                    |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                    |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                    |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                    |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                     |
| richards                   | 47.5 ms                                                | 33.3 ms: 1.43x faster                                                    |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                     |
| richards_super             | 53.7 ms                                                | 38.3 ms: 1.40x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                     |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                     |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                                    |
| float                      | 78.7 ms                                                | 64.2 ms: 1.22x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| spectral_norm              | 113 ms                                                 | 97.9 ms: 1.16x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                     |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                     |
| scimark_fft                | 367 ms                                                 | 332 ms: 1.10x faster                                                     |
| pylint                     | 312 ms                                                 | 285 ms: 1.10x faster                                                     |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                    |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 61.2 ms: 1.06x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 213 us                                                 | 203 us: 1.05x faster                                                     |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                    |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                    |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                    |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                    |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                    |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.9 ms: 1.01x faster                                                    |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                    |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                    |
| json                       | 5.32 ms                                                | 5.37 ms: 1.01x slower                                                    |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.16 ms: 1.03x slower                                                    |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                    |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                   |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                     |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                     |
| nbody                      | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                     |
| fannkuch                   | 394 ms                                                 | 420 ms: 1.07x slower                                                     |
| generators                 | 28.8 ms                                                | 30.8 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.60 ms: 1.09x slower                                                    |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                    |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                    |
| comprehensions             | 16.5 us                                                | 18.0 us: 1.09x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 902 us: 1.10x slower                                                     |
| logging_simple             | 5.65 us                                                | 6.28 us: 1.11x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 812 ms: 1.12x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                   |
| logging_format             | 6.23 us                                                | 7.08 us: 1.14x slower                                                    |
| many_optionals             | 857 us                                                 | 994 us: 1.16x slower                                                     |
| subparsers                 | 15.5 ms                                                | 24.0 ms: 1.55x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 93.0 ms: 3.88x slower                                                    |
| logging_silent             | 101 ns                                                 | 469 ns: 4.64x slower                                                     |
| coverage                   | 82.8 ms                                                | 427 ms: 5.16x slower                                                     |
| thrift                     | 800 us                                                 | 148 ms: 185.42x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                             |

Benchmark hidden because not significant (7): sphinx, sympy_sum, connected_components, sympy_str, mako, asyncio_websockets, shortest_path
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250521-3.15.0a0-0e20c44-JIT/bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 98.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x