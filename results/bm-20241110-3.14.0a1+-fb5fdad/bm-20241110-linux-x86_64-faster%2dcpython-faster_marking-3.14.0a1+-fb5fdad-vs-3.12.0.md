# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: fb5fdad
- commit date: 2024-11-10
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.85x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                      |
| nbody          | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                      |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 99.9 ms: 1.07x faster                                                      |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.83 ms: 1.02x faster                                                      |
| python_startup         | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                      |
| django_template | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 3.79 ms                                                | 1.89 ms: 2.01x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.85x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                       |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                       |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                      |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                      |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                       |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                      |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                      |
| float                      | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.9 ms: 1.07x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                      |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 65.3 ms: 1.05x faster                                                      |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                     |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                      |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                       |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                       |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                      |
| python_startup_no_site     | 6.94 ms                                                | 6.83 ms: 1.02x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.99 ms: 1.01x faster                                                      |
| nbody                      | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.01x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.40 ms: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                       |
| django_template            | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 856 us: 1.02x slower                                                       |
| richards                   | 45.8 ms                                                | 46.6 ms: 1.02x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                       |
| richards_super             | 51.5 ms                                                | 53.0 ms: 1.03x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                      |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.03x slower                                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                      |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241110-3.14.0a1+-fb5fdad/bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.108x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x