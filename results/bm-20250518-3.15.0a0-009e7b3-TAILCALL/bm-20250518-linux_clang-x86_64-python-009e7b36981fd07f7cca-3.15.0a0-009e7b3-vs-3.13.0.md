# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-x86_64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.010x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                  |
| async_tree_io              | 838 ms                                                 | 587 ms: 1.43x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.37x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 392 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.09x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                 |
| nbody          | 87.7 ms                                                | 84.8 ms: 1.03x faster                                                 |
| pidigits       | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                 | 198 ms: 1.11x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                 |
| regex_compile  | 132 ms                                                 | 123 ms: 1.07x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 305 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 88.0 ms: 1.01x slower                                                 |
| xml_etree_parse      | 154 ms                                                 | 160 ms: 1.04x slower                                                  |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                 |
| genshi_xml     | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| mako           | 10.7 ms                                                | 12.1 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.09x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                  |
| deepcopy                   | 354 us                                                 | 245 us: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 587 ms: 1.43x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.37x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                                 |
| go                         | 141 ms                                                 | 106 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.55 us: 1.27x faster                                                 |
| spectral_norm              | 113 ms                                                 | 94.4 ms: 1.20x faster                                                 |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                  |
| richards                   | 47.5 ms                                                | 40.4 ms: 1.18x faster                                                 |
| float                      | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                 |
| telco                      | 8.40 ms                                                | 7.30 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.38 ms: 1.15x faster                                                 |
| pathlib                    | 17.4 ms                                                | 15.2 ms: 1.14x faster                                                 |
| richards_super             | 53.7 ms                                                | 47.0 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| scimark_sor                | 122 ms                                                 | 107 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 59.2 ms: 1.13x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 57.9 ms: 1.12x faster                                                 |
| regex_dna                  | 220 ms                                                 | 198 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 392 ms: 1.10x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.31 sec: 1.09x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 18.3 ms: 1.08x faster                                                 |
| chaos                      | 58.0 ms                                                | 53.6 ms: 1.08x faster                                                 |
| deltablue                  | 3.19 ms                                                | 2.95 ms: 1.08x faster                                                 |
| hexiom                     | 6.08 ms                                                | 5.67 ms: 1.07x faster                                                 |
| regex_compile              | 132 ms                                                 | 123 ms: 1.07x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 108 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                 |
| sympy_str                  | 273 ms                                                 | 260 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 144 ms: 1.05x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                 |
| nbody                      | 87.7 ms                                                | 84.8 ms: 1.03x faster                                                 |
| raytrace                   | 262 ms                                                 | 254 ms: 1.03x faster                                                  |
| sympy_expand               | 456 ms                                                 | 443 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.9 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                |
| nqueens                    | 80.9 ms                                                | 79.2 ms: 1.02x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                 |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 305 us: 1.01x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                  |
| json                       | 5.32 ms                                                | 5.39 ms: 1.01x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 88.0 ms: 1.01x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.01x slower                                                 |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                  |
| shortest_path              | 487 ms                                                 | 502 ms: 1.03x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 160 ms: 1.04x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 756 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                |
| connected_components       | 447 ms                                                 | 465 ms: 1.04x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 852 us: 1.04x slower                                                  |
| meteor_contest             | 108 ms                                                 | 113 ms: 1.04x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.96 us: 1.05x slower                                                 |
| logging_format             | 6.23 us                                                | 6.72 us: 1.08x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                                 |
| pidigits                   | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                                  |
| mako                       | 10.7 ms                                                | 12.1 ms: 1.13x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.3 ms: 1.51x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 92.7 ms: 3.86x slower                                                 |
| coverage                   | 82.8 ms                                                | 399 ms: 4.82x slower                                                  |
| logging_silent             | 101 ns                                                 | 503 ns: 4.98x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 185.11x slower                                                |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, django_template
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (21) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x