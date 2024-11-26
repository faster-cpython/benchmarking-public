# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: b20a4b8
- commit date: 2024-11-14
- overall geometric mean: 1.141x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 1.29 sec: 4.84x slower                                               |
| docutils       | 2.59 sec                                               | 6.96 sec: 2.68x slower                                               |
| html5lib       | 64.2 ms                                                | 69.5 ms: 1.08x slower                                                |
| sphinx         | 1.03 sec                                               | 3.03 sec: 2.93x slower                                               |
| Geometric mean | (ref)                                                  | 2.53x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 382 ms: 1.21x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                 |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.03x faster                                                 |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                 |
| async_tree_io              | 842 ms                                                 | 870 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 464 ms: 1.07x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 980 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| float          | 79.2 ms                                                | 80.1 ms: 1.01x slower                                                |
| nbody          | 87.0 ms                                                | 89.5 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                 | 214 ms: 1.02x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.66 ms: 1.02x faster                                                |
| regex_compile  | 132 ms                                                 | 229 ms: 1.73x slower                                                 |
| regex_v8       | 26.2 ms                                                | 48.4 ms: 1.85x slower                                                |
| Geometric mean | (ref)                                                  | 1.32x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.05 sec: 1.05x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 83.1 ms: 1.04x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                 |
| unpickle_pure_python | 216 us                                                 | 231 us: 1.07x slower                                                 |
| json_loads           | 27.2 us                                                | 34.2 us: 1.25x slower                                                |
| json_dumps           | 10.6 ms                                                | 13.7 ms: 1.29x slower                                                |
| pickle_pure_python   | 310 us                                                 | 628 us: 2.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.7 ms: 1.03x faster                                                |
| django_template | 35.2 ms                                                | 34.3 ms: 1.02x faster                                                |
| genshi_text     | 23.5 ms                                                | 26.2 ms: 1.11x slower                                                |
| genshi_xml      | 50.9 ms                                                | 60.6 ms: 1.19x slower                                                |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 284 us: 1.26x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 31.9 us: 1.22x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 382 ms: 1.21x faster                                                 |
| richards_super             | 54.9 ms                                                | 47.7 ms: 1.15x faster                                                |
| richards                   | 48.7 ms                                                | 42.9 ms: 1.13x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.83 us: 1.13x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                |
| scimark_fft                | 364 ms                                                 | 338 ms: 1.08x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 71.9 ms: 1.05x faster                                                |
| tomli_loads                | 2.14 sec                                               | 2.05 sec: 1.05x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 83.1 ms: 1.04x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.03x faster                                                 |
| mako                       | 11.1 ms                                                | 10.7 ms: 1.03x faster                                                |
| mdp                        | 2.72 sec                                               | 2.65 sec: 1.02x faster                                               |
| django_template            | 35.2 ms                                                | 34.3 ms: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.94 ms: 1.02x faster                                                |
| regex_dna                  | 218 ms                                                 | 214 ms: 1.02x faster                                                 |
| regex_effbot               | 3.73 ms                                                | 3.66 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.66 sec: 1.02x faster                                               |
| go                         | 144 ms                                                 | 141 ms: 1.02x faster                                                 |
| logging_format             | 6.40 us                                                | 6.31 us: 1.01x faster                                                |
| coverage                   | 84.0 ms                                                | 83.2 ms: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 67.9 ms: 1.01x slower                                                |
| logging_simple             | 5.72 us                                                | 5.78 us: 1.01x slower                                                |
| float                      | 79.2 ms                                                | 80.1 ms: 1.01x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.49 ms: 1.03x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                |
| connected_components       | 444 ms                                                 | 456 ms: 1.03x slower                                                 |
| nbody                      | 87.0 ms                                                | 89.5 ms: 1.03x slower                                                |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                 |
| async_tree_io              | 842 ms                                                 | 870 ms: 1.03x slower                                                 |
| shortest_path              | 481 ms                                                 | 498 ms: 1.04x slower                                                 |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 165 us                                                 | 172 us: 1.04x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 763 ms: 1.05x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.9 ms: 1.05x slower                                                |
| pprint_pformat             | 1.49 sec                                               | 1.58 sec: 1.06x slower                                               |
| async_generators           | 436 ms                                                 | 464 ms: 1.07x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.28 sec: 1.07x slower                                               |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 231 us: 1.07x slower                                                 |
| raytrace                   | 267 ms                                                 | 286 ms: 1.07x slower                                                 |
| chaos                      | 58.1 ms                                                | 62.6 ms: 1.08x slower                                                |
| html5lib                   | 64.2 ms                                                | 69.5 ms: 1.08x slower                                                |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.73 ms: 1.09x slower                                                |
| bench_thread_pool          | 822 us                                                 | 906 us: 1.10x slower                                                 |
| genshi_text                | 23.5 ms                                                | 26.2 ms: 1.11x slower                                                |
| deltablue                  | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 980 ms: 1.14x slower                                                 |
| pyflate                    | 471 ms                                                 | 543 ms: 1.15x slower                                                 |
| nqueens                    | 78.4 ms                                                | 91.1 ms: 1.16x slower                                                |
| json                       | 5.36 ms                                                | 6.27 ms: 1.17x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 60.6 ms: 1.19x slower                                                |
| telco                      | 8.54 ms                                                | 10.5 ms: 1.23x slower                                                |
| hexiom                     | 6.16 ms                                                | 7.65 ms: 1.24x slower                                                |
| json_loads                 | 27.2 us                                                | 34.2 us: 1.25x slower                                                |
| json_dumps                 | 10.6 ms                                                | 13.7 ms: 1.29x slower                                                |
| sympy_expand               | 463 ms                                                 | 601 ms: 1.30x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 26.5 ms: 1.33x slower                                                |
| thrift                     | 809 us                                                 | 1.09 ms: 1.35x slower                                                |
| generators                 | 29.0 ms                                                | 39.7 ms: 1.37x slower                                                |
| dulwich_log                | 64.3 ms                                                | 97.0 ms: 1.51x slower                                                |
| k_core                     | 2.35 sec                                               | 3.66 sec: 1.56x slower                                               |
| sympy_str                  | 275 ms                                                 | 457 ms: 1.66x slower                                                 |
| regex_compile              | 132 ms                                                 | 229 ms: 1.73x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 197 ms: 1.83x slower                                                 |
| regex_v8                   | 26.2 ms                                                | 48.4 ms: 1.85x slower                                                |
| pickle_pure_python         | 310 us                                                 | 628 us: 2.02x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 317 ms: 2.11x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 283 ms: 2.12x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 142 ms: 2.64x slower                                                 |
| docutils                   | 2.59 sec                                               | 6.96 sec: 2.68x slower                                               |
| sphinx                     | 1.03 sec                                               | 3.03 sec: 2.93x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 108 ms: 4.50x slower                                                 |
| 2to3                       | 267 ms                                                 | 1.29 sec: 4.84x slower                                               |
| pylint                     | 313 ms                                                 | 2.05 sec: 6.57x slower                                               |
| Geometric mean             | (ref)                                                  | 1.19x slower                                                         |

Benchmark hidden because not significant (5): xml_etree_process, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, fannkuch
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241114-3.14.0a1+-b20a4b8-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8.json: djangocms, sqlite_synth

- Geometric mean (including insignificant results): 1.141x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.12x