# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: a94d30d
- commit date: 2024-11-09
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 640 ms: 1.85x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 629 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.76x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.2 ms: 1.07x faster                                                      |
| nbody          | 97.0 ms                                                | 95.1 ms: 1.02x faster                                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| json_loads           | 28.5 us                                                | 26.0 us: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.78 ms: 1.02x faster                                                      |
| python_startup         | 9.55 ms                                                | 12.3 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                      |
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 3.79 ms                                                | 1.97 ms: 1.93x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 640 ms: 1.85x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 629 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.76x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                       |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                      |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                      |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                       |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                      |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| json                       | 5.26 ms                                                | 4.79 ms: 1.10x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.09x faster                                                      |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                      |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                      |
| float                      | 84.7 ms                                                | 79.2 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                       |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                      |
| pyflate                    | 482 ms                                                 | 466 ms: 1.03x faster                                                       |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                       |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                                      |
| python_startup_no_site     | 6.94 ms                                                | 6.78 ms: 1.02x faster                                                      |
| nbody                      | 97.0 ms                                                | 95.1 ms: 1.02x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 54.1 ms: 1.01x faster                                                      |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                       |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                       |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                       |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                      |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                       |
| richards_super             | 51.5 ms                                                | 52.6 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.17 ms: 1.02x slower                                                      |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                      |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.10x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                                      |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.16x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.3 ms: 1.29x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (5): scimark_fft, regex_effbot, asyncio_websockets, coroutines, richards
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-a94d30d/bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.113x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x