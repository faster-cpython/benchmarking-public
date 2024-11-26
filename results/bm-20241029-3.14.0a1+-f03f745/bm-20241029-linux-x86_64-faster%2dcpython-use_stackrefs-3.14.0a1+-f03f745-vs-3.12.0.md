# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                    |
| tornado_http   | 103 ms                                                 | 92.5 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                      |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 326 ms: 1.38x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 574 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 583 ms: 1.24x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 989 ms: 1.20x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 81.1 ms: 1.05x faster                                                     |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                    |
| json_loads           | 28.5 us                                                | 26.5 us: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.33x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                     |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                      |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                      |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 326 ms: 1.38x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.32x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 574 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 583 ms: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 989 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                     |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                      |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                     |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                    |
| tornado_http               | 103 ms                                                 | 92.5 ms: 1.11x faster                                                     |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                     |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.5 ms: 1.08x faster                                                     |
| json                       | 5.26 ms                                                | 4.89 ms: 1.08x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.5 us: 1.07x faster                                                     |
| chaos                      | 67.0 ms                                                | 62.5 ms: 1.07x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                     |
| async_generators           | 463 ms                                                 | 439 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                    |
| float                      | 84.7 ms                                                | 81.1 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                      |
| scimark_fft                | 382 ms                                                 | 370 ms: 1.03x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                     |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 763 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                                      |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.00x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.7 ms: 1.00x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.57 sec: 1.00x slower                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.09 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                      |
| richards                   | 45.8 ms                                                | 46.2 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 858 us: 1.02x slower                                                      |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                                     |
| fannkuch                   | 417 ms                                                 | 427 ms: 1.02x slower                                                      |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| scimark_sor                | 129 ms                                                 | 135 ms: 1.04x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.55 ms: 1.20x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.33x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 79.1 ms: 3.29x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_parse, sqlite_synth, sqlglot_normalize, pyflate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.052x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x