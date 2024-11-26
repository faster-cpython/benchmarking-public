# Results vs. base

- fork: faster-cpython
- ref: eager_dict_tracking
- machine: linux-x86_64
- commit hash: 498979f
- commit date: 2024-11-19
- overall geometric mean: 1.008x faster
- HPT reliability: 97.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.00x slower                                                            |
| docutils       | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                          |
| html5lib       | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg          | 984 ms                                                                 | 915 ms: 1.08x faster                                                            |
| async_tree_none           | 330 ms                                                                 | 321 ms: 1.03x faster                                                            |
| async_generators          | 427 ms                                                                 | 430 ms: 1.01x slower                                                            |
| async_tree_memoization_tg | 379 ms                                                                 | 399 ms: 1.05x slower                                                            |
| async_tree_io             | 859 ms                                                                 | 906 ms: 1.05x slower                                                            |
| Geometric mean            | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 96.9 ms                                                                | 92.9 ms: 1.04x faster                                                           |
| pidigits       | 188 ms                                                                 | 187 ms: 1.01x faster                                                            |
| float          | 80.8 ms                                                                | 81.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 226 ms                                                                 | 223 ms: 1.01x faster                                                            |
| regex_v8       | 26.5 ms                                                                | 26.3 ms: 1.01x faster                                                           |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                            |
| regex_effbot   | 3.51 ms                                                                | 3.48 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                 | 151 ms: 1.05x faster                                                            |
| pickle_pure_python   | 328 us                                                                 | 323 us: 1.02x faster                                                            |
| xml_etree_generate   | 86.8 ms                                                                | 86.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 219 us                                                                 | 218 us: 1.01x faster                                                            |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                           |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.7 ms                                                                | 11.4 ms: 1.03x faster                                                           |
| genshi_text    | 22.2 ms                                                                | 22.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                 | bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1+-30aeb00 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| k_core                    | 3.63 sec                                                               | 2.92 sec: 1.24x faster                                                          |
| pylint                    | 320 ms                                                                 | 262 ms: 1.22x faster                                                            |
| gc_traversal              | 4.83 ms                                                                | 4.31 ms: 1.12x faster                                                           |
| async_tree_io_tg          | 984 ms                                                                 | 915 ms: 1.08x faster                                                            |
| xml_etree_parse           | 159 ms                                                                 | 151 ms: 1.05x faster                                                            |
| nbody                     | 96.9 ms                                                                | 92.9 ms: 1.04x faster                                                           |
| pycparser                 | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                                          |
| mako                      | 11.7 ms                                                                | 11.4 ms: 1.03x faster                                                           |
| async_tree_none           | 330 ms                                                                 | 321 ms: 1.03x faster                                                            |
| fannkuch                  | 413 ms                                                                 | 403 ms: 1.03x faster                                                            |
| hexiom                    | 6.35 ms                                                                | 6.22 ms: 1.02x faster                                                           |
| create_gc_cycles          | 2.69 ms                                                                | 2.64 ms: 1.02x faster                                                           |
| scimark_lu                | 117 ms                                                                 | 116 ms: 1.02x faster                                                            |
| pickle_pure_python        | 328 us                                                                 | 323 us: 1.02x faster                                                            |
| sympy_expand              | 464 ms                                                                 | 457 ms: 1.02x faster                                                            |
| regex_dna                 | 226 ms                                                                 | 223 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult   | 4.83 ms                                                                | 4.76 ms: 1.01x faster                                                           |
| thrift                    | 781 us                                                                 | 770 us: 1.01x faster                                                            |
| spectral_norm             | 116 ms                                                                 | 114 ms: 1.01x faster                                                            |
| json                      | 5.02 ms                                                                | 4.96 ms: 1.01x faster                                                           |
| scimark_fft               | 369 ms                                                                 | 365 ms: 1.01x faster                                                            |
| sympy_str                 | 270 ms                                                                 | 267 ms: 1.01x faster                                                            |
| deepcopy                  | 262 us                                                                 | 259 us: 1.01x faster                                                            |
| xml_etree_generate        | 86.8 ms                                                                | 86.0 ms: 1.01x faster                                                           |
| shortest_path             | 480 ms                                                                 | 476 ms: 1.01x faster                                                            |
| generators                | 27.8 ms                                                                | 27.6 ms: 1.01x faster                                                           |
| regex_v8                  | 26.5 ms                                                                | 26.3 ms: 1.01x faster                                                           |
| regex_compile             | 130 ms                                                                 | 129 ms: 1.01x faster                                                            |
| docutils                  | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                          |
| dulwich_log               | 65.4 ms                                                                | 64.9 ms: 1.01x faster                                                           |
| html5lib                  | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                                           |
| meteor_contest            | 108 ms                                                                 | 107 ms: 1.01x faster                                                            |
| logging_format            | 6.21 us                                                                | 6.17 us: 1.01x faster                                                           |
| regex_effbot              | 3.51 ms                                                                | 3.48 ms: 1.01x faster                                                           |
| deepcopy_memo             | 31.0 us                                                                | 30.8 us: 1.01x faster                                                           |
| crypto_pyaes              | 74.0 ms                                                                | 73.6 ms: 1.01x faster                                                           |
| sympy_sum                 | 147 ms                                                                 | 147 ms: 1.01x faster                                                            |
| pidigits                  | 188 ms                                                                 | 187 ms: 1.01x faster                                                            |
| unpickle_pure_python      | 219 us                                                                 | 218 us: 1.01x faster                                                            |
| pathlib                   | 16.0 ms                                                                | 15.9 ms: 1.00x faster                                                           |
| sqlglot_optimize          | 53.6 ms                                                                | 53.3 ms: 1.00x faster                                                           |
| bench_mp_pool             | 78.9 ms                                                                | 78.5 ms: 1.00x faster                                                           |
| nqueens                   | 80.2 ms                                                                | 80.0 ms: 1.00x faster                                                           |
| sqlglot_normalize         | 107 ms                                                                 | 107 ms: 1.00x faster                                                            |
| python_startup_no_site    | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                           |
| 2to3                      | 256 ms                                                                 | 257 ms: 1.00x slower                                                            |
| comprehensions            | 16.9 us                                                                | 17.0 us: 1.00x slower                                                           |
| async_generators          | 427 ms                                                                 | 430 ms: 1.01x slower                                                            |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                           |
| pprint_pformat            | 1.49 sec                                                               | 1.50 sec: 1.01x slower                                                          |
| genshi_text               | 22.2 ms                                                                | 22.3 ms: 1.01x slower                                                           |
| richards_super            | 53.2 ms                                                                | 53.6 ms: 1.01x slower                                                           |
| bpe_tokeniser             | 4.74 sec                                                               | 4.78 sec: 1.01x slower                                                          |
| float                     | 80.8 ms                                                                | 81.6 ms: 1.01x slower                                                           |
| typing_runtime_protocols  | 162 us                                                                 | 164 us: 1.01x slower                                                            |
| telco                     | 7.83 ms                                                                | 7.94 ms: 1.01x slower                                                           |
| richards                  | 46.9 ms                                                                | 47.6 ms: 1.01x slower                                                           |
| deltablue                 | 3.32 ms                                                                | 3.38 ms: 1.02x slower                                                           |
| subparsers                | 20.7 ms                                                                | 21.0 ms: 1.02x slower                                                           |
| json_dumps                | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                           |
| coverage                  | 83.9 ms                                                                | 85.5 ms: 1.02x slower                                                           |
| pyflate                   | 460 ms                                                                 | 469 ms: 1.02x slower                                                            |
| go                        | 119 ms                                                                 | 123 ms: 1.03x slower                                                            |
| logging_silent            | 105 ns                                                                 | 110 ns: 1.04x slower                                                            |
| async_tree_memoization_tg | 379 ms                                                                 | 399 ms: 1.05x slower                                                            |
| async_tree_io             | 859 ms                                                                 | 906 ms: 1.05x slower                                                            |
| mdp                       | 2.51 sec                                                               | 2.68 sec: 1.07x slower                                                          |
| Geometric mean            | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (30): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, connected_components, sqlalchemy_imperative, deepcopy_reduce, logging_simple, genshi_xml, many_optionals, xml_etree_process, json_loads, sympy_integrate, raytrace, asyncio_websockets, sqlite_synth, scimark_monte_carlo, xml_etree_iterparse, scimark_sor, chaos, bench_thread_pool, sphinx, sqlalchemy_declarative, tomli_loads, sqlglot_transpile, pprint_safe_repr, coroutines, sqlglot_parse, djangocms, async_tree_cpu_io_mixed_tg, django_template

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 97.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x