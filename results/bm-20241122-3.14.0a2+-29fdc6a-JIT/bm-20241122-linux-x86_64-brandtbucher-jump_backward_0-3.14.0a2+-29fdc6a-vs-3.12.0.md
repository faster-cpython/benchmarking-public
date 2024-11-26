# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 29fdc6a
- commit date: 2024-11-22
- overall geometric mean: 1.035x faster
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                    |
| docutils       | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 412 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 328 ms: 1.37x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.36x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 582 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 586 ms: 1.24x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                   |
| float          | 84.7 ms                                                | 77.4 ms: 1.09x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                   |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.19x faster                                                  |
| json_loads           | 28.5 us                                                | 26.0 us: 1.10x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                   |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 412 ms: 1.39x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 328 ms: 1.37x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.36x faster                                                    |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 582 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 586 ms: 1.24x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                    |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 62.4 ms: 1.20x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.19x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                   |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.90 us: 1.15x faster                                                   |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.58 ms: 1.10x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                    |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.10x faster                                                   |
| float                      | 84.7 ms                                                | 77.4 ms: 1.09x faster                                                   |
| json                       | 5.26 ms                                                | 4.84 ms: 1.09x faster                                                   |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                    |
| chaos                      | 67.0 ms                                                | 61.8 ms: 1.08x faster                                                   |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                    |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                   |
| raytrace                   | 312 ms                                                 | 294 ms: 1.06x faster                                                    |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                    |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                                    |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                    |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                    |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 69.0 ms: 1.01x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                  |
| richards                   | 45.8 ms                                                | 46.7 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                   |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                   |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                    |
| logging_format             | 7.23 us                                                | 7.46 us: 1.03x slower                                                   |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                   |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                    |
| telco                      | 7.10 ms                                                | 7.46 ms: 1.05x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                   |
| deltablue                  | 3.72 ms                                                | 3.93 ms: 1.06x slower                                                   |
| logging_simple             | 6.46 us                                                | 6.84 us: 1.06x slower                                                   |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.80 ms: 1.07x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.4 ms: 1.08x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.2 ms: 1.08x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.09x slower                                                    |
| nqueens                    | 83.3 ms                                                | 90.8 ms: 1.09x slower                                                   |
| docutils                   | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 923 us: 1.10x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| hexiom                     | 6.41 ms                                                | 7.40 ms: 1.15x slower                                                   |
| coroutines                 | 23.2 ms                                                | 27.1 ms: 1.17x slower                                                   |
| generators                 | 31.2 ms                                                | 36.9 ms: 1.18x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                                   |
| coverage                   | 72.7 ms                                                | 87.9 ms: 1.21x slower                                                   |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): pickle_pure_python, mdp, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-29fdc6a-JIT/bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 99.42% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x