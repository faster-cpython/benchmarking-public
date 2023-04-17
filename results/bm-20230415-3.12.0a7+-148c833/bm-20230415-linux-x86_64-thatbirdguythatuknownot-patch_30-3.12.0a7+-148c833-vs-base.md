
# Results vs. base

- fork: thatbirdguythatuknownot
- ref: patch_30
- machine: linux-x86_64
- commit hash: 148c833
- commit date: 2023-04-15
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 249 ms: 1.00x faster                                                        |
| chameleon      | 6.32 ms                                                                | 6.48 ms: 1.03x slower                                                       |
| tornado_http   | 92.4 ms                                                                | 93.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 84.6 ms                                                                | 83.5 ms: 1.01x faster                                                       |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x faster                                                        |
| float          | 73.1 ms                                                                | 73.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                                | 21.8 ms: 1.02x faster                                                       |
| regex_compile  | 131 ms                                                                 | 129 ms: 1.01x faster                                                        |
| regex_dna      | 205 ms                                                                 | 207 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 4.35 us                                                                | 4.24 us: 1.03x faster                                                       |
| pickle               | 10.9 us                                                                | 10.7 us: 1.02x faster                                                       |
| unpickle_pure_python | 205 us                                                                 | 202 us: 1.01x faster                                                        |
| pickle_dict          | 32.2 us                                                                | 31.7 us: 1.01x faster                                                       |
| pickle_pure_python   | 289 us                                                                 | 286 us: 1.01x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                                | 79.8 ms: 1.01x faster                                                       |
| json_dumps           | 9.36 ms                                                                | 9.32 ms: 1.01x faster                                                       |
| json_loads           | 24.1 us                                                                | 24.4 us: 1.01x slower                                                       |
| unpickle             | 13.9 us                                                                | 14.3 us: 1.03x slower                                                       |
| unpickle_list        | 4.93 us                                                                | 5.15 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.86 ms                                                                | 8.90 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.57 ms                                                                | 6.60 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.2 ms                                                                | 9.96 ms: 1.02x faster                                                       |
| genshi_xml     | 46.5 ms                                                                | 47.1 ms: 1.01x slower                                                       |
| genshi_text    | 21.0 ms                                                                | 21.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230415-linux-x86_64-python-2b6f5c3483597abcb842-3.12.0a7+-2b6f5c3 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                     | 2.68 sec                                                               | 2.55 sec: 1.05x faster                                                      |
| pycparser               | 1.14 sec                                                               | 1.10 sec: 1.04x faster                                                      |
| unpack_sequence         | 44.5 ns                                                                | 42.9 ns: 1.04x faster                                                       |
| gc_traversal            | 4.18 ms                                                                | 4.06 ms: 1.03x faster                                                       |
| pickle_list             | 4.35 us                                                                | 4.24 us: 1.03x faster                                                       |
| spectral_norm           | 93.8 ms                                                                | 91.4 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult | 4.13 ms                                                                | 4.03 ms: 1.02x faster                                                       |
| scimark_monte_carlo     | 67.8 ms                                                                | 66.2 ms: 1.02x faster                                                       |
| regex_v8                | 22.3 ms                                                                | 21.8 ms: 1.02x faster                                                       |
| pickle                  | 10.9 us                                                                | 10.7 us: 1.02x faster                                                       |
| mako                    | 10.2 ms                                                                | 9.96 ms: 1.02x faster                                                       |
| coroutines              | 22.2 ms                                                                | 21.7 ms: 1.02x faster                                                       |
| scimark_sor             | 112 ms                                                                 | 110 ms: 1.02x faster                                                        |
| sqlglot_parse           | 1.24 ms                                                                | 1.22 ms: 1.02x faster                                                       |
| comprehensions          | 21.7 us                                                                | 21.4 us: 1.02x faster                                                       |
| unpickle_pure_python    | 205 us                                                                 | 202 us: 1.01x faster                                                        |
| pickle_dict             | 32.2 us                                                                | 31.7 us: 1.01x faster                                                       |
| nbody                   | 84.6 ms                                                                | 83.5 ms: 1.01x faster                                                       |
| pickle_pure_python      | 289 us                                                                 | 286 us: 1.01x faster                                                        |
| dask                    | 497 ms                                                                 | 491 ms: 1.01x faster                                                        |
| sqlglot_transpile       | 1.52 ms                                                                | 1.50 ms: 1.01x faster                                                       |
| regex_compile           | 131 ms                                                                 | 129 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 51.7 ms                                                                | 51.2 ms: 1.01x faster                                                       |
| scimark_lu              | 106 ms                                                                 | 105 ms: 1.01x faster                                                        |
| async_generators        | 431 ms                                                                 | 427 ms: 1.01x faster                                                        |
| xml_etree_generate      | 80.5 ms                                                                | 79.8 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.48 ms                                                                | 1.47 ms: 1.01x faster                                                       |
| logging_silent          | 96.5 ns                                                                | 95.8 ns: 1.01x faster                                                       |
| json_dumps              | 9.36 ms                                                                | 9.32 ms: 1.01x faster                                                       |
| 2to3                    | 250 ms                                                                 | 249 ms: 1.00x faster                                                        |
| deltablue               | 3.24 ms                                                                | 3.23 ms: 1.00x faster                                                       |
| asyncio_tcp             | 502 ms                                                                 | 500 ms: 1.00x faster                                                        |
| sqlglot_normalize       | 104 ms                                                                 | 104 ms: 1.00x faster                                                        |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x faster                                                        |
| bench_thread_pool       | 783 us                                                                 | 786 us: 1.00x slower                                                        |
| python_startup          | 8.86 ms                                                                | 8.90 ms: 1.00x slower                                                       |
| python_startup_no_site  | 6.57 ms                                                                | 6.60 ms: 1.00x slower                                                       |
| sympy_sum               | 162 ms                                                                 | 163 ms: 1.01x slower                                                        |
| logging_format          | 6.32 us                                                                | 6.36 us: 1.01x slower                                                       |
| tornado_http            | 92.4 ms                                                                | 93.0 ms: 1.01x slower                                                       |
| dulwich_log             | 61.9 ms                                                                | 62.3 ms: 1.01x slower                                                       |
| gunicorn                | 1.07 ms                                                                | 1.08 ms: 1.01x slower                                                       |
| sympy_str               | 279 ms                                                                 | 281 ms: 1.01x slower                                                        |
| float                   | 73.1 ms                                                                | 73.7 ms: 1.01x slower                                                       |
| pathlib                 | 17.0 ms                                                                | 17.2 ms: 1.01x slower                                                       |
| raytrace                | 279 ms                                                                 | 282 ms: 1.01x slower                                                        |
| crypto_pyaes            | 73.9 ms                                                                | 74.5 ms: 1.01x slower                                                       |
| json_loads              | 24.1 us                                                                | 24.4 us: 1.01x slower                                                       |
| sqlite_synth            | 2.61 us                                                                | 2.64 us: 1.01x slower                                                       |
| thrift                  | 785 us                                                                 | 792 us: 1.01x slower                                                        |
| sympy_integrate         | 20.2 ms                                                                | 20.4 ms: 1.01x slower                                                       |
| deepcopy                | 330 us                                                                 | 334 us: 1.01x slower                                                        |
| deepcopy_memo           | 34.5 us                                                                | 34.9 us: 1.01x slower                                                       |
| regex_dna               | 205 ms                                                                 | 207 ms: 1.01x slower                                                        |
| fannkuch                | 383 ms                                                                 | 387 ms: 1.01x slower                                                        |
| richards                | 41.8 ms                                                                | 42.3 ms: 1.01x slower                                                       |
| sympy_expand            | 452 ms                                                                 | 459 ms: 1.01x slower                                                        |
| genshi_xml              | 46.5 ms                                                                | 47.1 ms: 1.01x slower                                                       |
| logging_simple          | 5.67 us                                                                | 5.76 us: 1.01x slower                                                       |
| scimark_fft             | 305 ms                                                                 | 310 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.41 sec                                                               | 1.44 sec: 1.02x slower                                                      |
| genshi_text             | 21.0 ms                                                                | 21.5 ms: 1.02x slower                                                       |
| generators              | 28.2 ms                                                                | 28.9 ms: 1.02x slower                                                       |
| chameleon               | 6.32 ms                                                                | 6.48 ms: 1.03x slower                                                       |
| unpickle                | 13.9 us                                                                | 14.3 us: 1.03x slower                                                       |
| deepcopy_reduce         | 2.92 us                                                                | 3.02 us: 1.03x slower                                                       |
| pprint_safe_repr        | 681 ms                                                                 | 704 ms: 1.03x slower                                                        |
| unpickle_list           | 4.93 us                                                                | 5.15 us: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (27): sqlalchemy_imperative, pyflate, async_tree_none, go, html5lib, django_template, async_tree_cpu_io_mixed, async_tree_memoization, coverage, xml_etree_process, sqlalchemy_declarative, async_tree_io, mypy2, regex_effbot, bench_mp_pool, hexiom, docutils, chaos, json, nqueens, aiohttp, meteor_contest, telco, xml_etree_iterparse, pylint, xml_etree_parse, djangocms
