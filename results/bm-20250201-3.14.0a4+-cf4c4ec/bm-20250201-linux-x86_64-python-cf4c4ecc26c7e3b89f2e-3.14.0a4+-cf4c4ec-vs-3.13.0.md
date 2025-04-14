# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                   |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.4 ms: 1.10x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 92.3 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.7 ms: 1.05x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.9 ms: 1.04x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 28.4 us: 1.05x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                  |
| genshi_xml     | 50.5 ms                                                | 48.2 ms: 1.05x faster                                                  |
| mako           | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                  |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                   |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                   |
| float                      | 78.7 ms                                                | 71.4 ms: 1.10x faster                                                  |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                                  |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                                  |
| scimark_fft                | 367 ms                                                 | 343 ms: 1.07x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.58 ms: 1.07x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.3 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                 |
| richards                   | 47.5 ms                                                | 45.0 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                  |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                   |
| richards_super             | 53.7 ms                                                | 51.1 ms: 1.05x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 48.2 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 25.7 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.9 ms: 1.04x faster                                                  |
| generators                 | 28.8 ms                                                | 27.5 ms: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.43 us: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 433 ms: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                 |
| logging_format             | 6.23 us                                                | 6.06 us: 1.03x faster                                                  |
| shortest_path              | 487 ms                                                 | 473 ms: 1.03x faster                                                   |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 52.0 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                                   |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                 |
| nqueens                    | 80.9 ms                                                | 80.1 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                  |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.9 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.22 ms: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.0 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| nbody                      | 87.7 ms                                                | 92.3 ms: 1.05x slower                                                  |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.07x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                  |
| coverage                   | 82.8 ms                                                | 91.1 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 947 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (8): sympy_expand, sympy_sum, create_gc_cycles, pyflate, sqlglot_transpile, comprehensions, asyncio_websockets, django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x