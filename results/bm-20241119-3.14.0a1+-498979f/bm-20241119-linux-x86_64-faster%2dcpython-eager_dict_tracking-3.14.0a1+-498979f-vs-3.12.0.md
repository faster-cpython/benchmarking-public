# Results vs. 3.12.0

- fork: faster-cpython
- ref: eager_dict_tracking
- machine: linux-x86_64
- commit hash: 498979f
- commit date: 2024-11-19
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                           |
| float          | 84.7 ms                                                | 81.6 ms: 1.04x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                           |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                          |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                            |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                                            |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.27x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                           |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                           |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                            |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                            |
| go                         | 139 ms                                                 | 123 ms: 1.14x faster                                                            |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                          |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                           |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                            |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                           |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 64.9 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.05x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.0 ms: 1.04x faster                                                           |
| float                      | 84.7 ms                                                | 81.6 ms: 1.04x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                           |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                           |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| scimark_sor                | 129 ms                                                 | 129 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                            |
| richards                   | 45.8 ms                                                | 47.6 ms: 1.04x slower                                                           |
| richards_super             | 51.5 ms                                                | 53.6 ms: 1.04x slower                                                           |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.31 ms: 1.14x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.5 ms: 1.18x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): spectral_norm, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241119-3.14.0a1+-498979f/bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.067x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x