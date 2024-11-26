# Results vs. 3.13.0

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.013x faster
- HPT reliability: 77.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.59 sec                                               | 2.68 sec: 1.03x slower                                                 |
| html5lib       | 64.2 ms                                                | 63.6 ms: 1.01x faster                                                  |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                                   |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                   |
| async_generators           | 436 ms                                                 | 431 ms: 1.01x faster                                                   |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                   |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 563 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| float          | 79.2 ms                                                | 79.9 ms: 1.01x slower                                                  |
| nbody          | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                  |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| regex_effbot   | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 59.7 ms: 1.02x faster                                                  |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                 |
| xml_etree_generate   | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                  |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                   |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                   |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                  |
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                  |
| genshi_text     | 23.5 ms                                                | 23.2 ms: 1.02x faster                                                  |
| mako            | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 264 us: 1.36x faster                                                   |
| deepcopy_memo              | 39.1 us                                                | 31.1 us: 1.26x faster                                                  |
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                                   |
| go                         | 144 ms                                                 | 120 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.74 us: 1.17x faster                                                  |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                  |
| json                       | 5.36 ms                                                | 4.87 ms: 1.10x faster                                                  |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                   |
| richards                   | 48.7 ms                                                | 45.7 ms: 1.07x faster                                                  |
| telco                      | 8.54 ms                                                | 8.02 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                   |
| richards_super             | 54.9 ms                                                | 52.0 ms: 1.06x faster                                                  |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                  |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                  |
| thrift                     | 809 us                                                 | 775 us: 1.04x faster                                                   |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                  |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.63 sec: 1.03x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                  |
| sympy_str                  | 275 ms                                                 | 266 ms: 1.03x faster                                                   |
| logging_format             | 6.40 us                                                | 6.21 us: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                                  |
| sympy_expand               | 463 ms                                                 | 452 ms: 1.03x faster                                                   |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 73.8 ms: 1.02x faster                                                  |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| genshi_text                | 23.5 ms                                                | 23.2 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 59.7 ms: 1.02x faster                                                  |
| dulwich_log                | 64.3 ms                                                | 63.4 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                   |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                 |
| async_generators           | 436 ms                                                 | 431 ms: 1.01x faster                                                   |
| html5lib                   | 64.2 ms                                                | 63.6 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.49 sec: 1.00x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.58 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| regex_effbot               | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                  |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                  |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                                   |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                   |
| float                      | 79.2 ms                                                | 79.9 ms: 1.01x slower                                                  |
| coverage                   | 84.0 ms                                                | 84.8 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                 | 270 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.82 sec: 1.02x slower                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                   |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                   |
| fannkuch                   | 404 ms                                                 | 414 ms: 1.02x slower                                                   |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                  |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                   |
| scimark_fft                | 364 ms                                                 | 374 ms: 1.03x slower                                                   |
| deltablue                  | 3.23 ms                                                | 3.32 ms: 1.03x slower                                                  |
| bench_thread_pool          | 822 us                                                 | 846 us: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 563 ms: 1.03x slower                                                   |
| docutils                   | 2.59 sec                                               | 2.68 sec: 1.03x slower                                                 |
| hexiom                     | 6.16 ms                                                | 6.37 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                   |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.04x slower                                                   |
| nqueens                    | 78.4 ms                                                | 81.7 ms: 1.04x slower                                                  |
| chaos                      | 58.1 ms                                                | 61.0 ms: 1.05x slower                                                  |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                  |
| nbody                      | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                  |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                  |
| gc_traversal               | 4.37 ms                                                | 4.73 ms: 1.08x slower                                                  |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 78.0 ms: 3.25x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, xml_etree_parse, pyflate, regex_dna, async_tree_none_tg, scimark_sparse_mat_mult, pprint_safe_repr, genshi_xml, sphinx, async_tree_io, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241018-3.14.0a1+-f8ba9fb/bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 77.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x