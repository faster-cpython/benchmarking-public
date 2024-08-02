# Results vs. base

- fork: brandtbucher
- ref: jump_to_top
- machine: linux-x86_64
- commit hash: 7bff512
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 87.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| html5lib       | 67.1 ms                                                               | 66.7 ms: 1.01x faster                                              |
| tornado_http   | 93.8 ms                                                               | 93.3 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 80.7 ms                                                               | 79.2 ms: 1.02x faster                                              |
| float          | 69.6 ms                                                               | 70.2 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                | 135 ms: 1.00x faster                                               |
| regex_dna      | 221 ms                                                                | 227 ms: 1.03x slower                                               |
| regex_effbot   | 3.56 ms                                                               | 3.85 ms: 1.08x slower                                              |
| regex_v8       | 23.1 ms                                                               | 26.8 ms: 1.16x slower                                              |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle            | 14.9 us                                                               | 14.4 us: 1.03x faster                                              |
| pickle_dict         | 35.7 us                                                               | 35.5 us: 1.01x faster                                              |
| pickle_pure_python  | 291 us                                                                | 290 us: 1.01x faster                                               |
| xml_etree_iterparse | 98.6 ms                                                               | 99.5 ms: 1.01x slower                                              |
| json_loads          | 28.5 us                                                               | 28.8 us: 1.01x slower                                              |
| pickle              | 11.7 us                                                               | 11.9 us: 1.02x slower                                              |
| unpickle_list       | 5.15 us                                                               | 5.28 us: 1.03x slower                                              |
| pickle_list         | 4.93 us                                                               | 5.31 us: 1.08x slower                                              |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (6): tomli_loads, json_dumps, xml_etree_parse, xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                              |
| python_startup_no_site | 7.41 ms                                                               | 7.39 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 37.4 ms                                                               | 36.6 ms: 1.02x faster                                              |
| mako            | 9.54 ms                                                               | 9.63 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                      | 2.76 sec                                                              | 2.53 sec: 1.09x faster                                             |
| gc_traversal             | 3.74 ms                                                               | 3.59 ms: 1.04x faster                                              |
| unpickle                 | 14.9 us                                                               | 14.4 us: 1.03x faster                                              |
| scimark_sparse_mat_mult  | 4.52 ms                                                               | 4.41 ms: 1.03x faster                                              |
| django_template          | 37.4 ms                                                               | 36.6 ms: 1.02x faster                                              |
| chaos                    | 60.4 ms                                                               | 59.2 ms: 1.02x faster                                              |
| sympy_expand             | 508 ms                                                                | 499 ms: 1.02x faster                                               |
| nbody                    | 80.7 ms                                                               | 79.2 ms: 1.02x faster                                              |
| scimark_lu               | 125 ms                                                                | 123 ms: 1.02x faster                                               |
| sympy_sum                | 168 ms                                                                | 165 ms: 1.02x faster                                               |
| raytrace                 | 275 ms                                                                | 271 ms: 1.01x faster                                               |
| sympy_integrate          | 22.3 ms                                                               | 22.0 ms: 1.01x faster                                              |
| typing_runtime_protocols | 169 us                                                                | 167 us: 1.01x faster                                               |
| sympy_str                | 297 ms                                                                | 294 ms: 1.01x faster                                               |
| thrift                   | 811 us                                                                | 804 us: 1.01x faster                                               |
| sqlglot_optimize         | 56.1 ms                                                               | 55.6 ms: 1.01x faster                                              |
| scimark_monte_carlo      | 62.2 ms                                                               | 61.6 ms: 1.01x faster                                              |
| bench_thread_pool        | 834 us                                                                | 827 us: 1.01x faster                                               |
| sqlite_synth             | 2.82 us                                                               | 2.80 us: 1.01x faster                                              |
| dulwich_log              | 67.6 ms                                                               | 67.1 ms: 1.01x faster                                              |
| html5lib                 | 67.1 ms                                                               | 66.7 ms: 1.01x faster                                              |
| pickle_dict              | 35.7 us                                                               | 35.5 us: 1.01x faster                                              |
| tornado_http             | 93.8 ms                                                               | 93.3 ms: 1.01x faster                                              |
| pickle_pure_python       | 291 us                                                                | 290 us: 1.01x faster                                               |
| create_gc_cycles         | 1.75 ms                                                               | 1.74 ms: 1.01x faster                                              |
| deltablue                | 3.54 ms                                                               | 3.52 ms: 1.00x faster                                              |
| scimark_fft              | 318 ms                                                                | 317 ms: 1.00x faster                                               |
| richards                 | 42.0 ms                                                               | 41.9 ms: 1.00x faster                                              |
| python_startup           | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                              |
| regex_compile            | 135 ms                                                                | 135 ms: 1.00x faster                                               |
| python_startup_no_site   | 7.41 ms                                                               | 7.39 ms: 1.00x faster                                              |
| sqlglot_transpile        | 1.60 ms                                                               | 1.61 ms: 1.00x slower                                              |
| async_generators         | 459 ms                                                                | 462 ms: 1.01x slower                                               |
| pathlib                  | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                              |
| fannkuch                 | 350 ms                                                                | 353 ms: 1.01x slower                                               |
| bpe_tokeniser            | 4.80 sec                                                              | 4.84 sec: 1.01x slower                                             |
| float                    | 69.6 ms                                                               | 70.2 ms: 1.01x slower                                              |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                              |
| crypto_pyaes             | 66.4 ms                                                               | 67.0 ms: 1.01x slower                                              |
| xml_etree_iterparse      | 98.6 ms                                                               | 99.5 ms: 1.01x slower                                              |
| json_loads               | 28.5 us                                                               | 28.8 us: 1.01x slower                                              |
| mako                     | 9.54 ms                                                               | 9.63 ms: 1.01x slower                                              |
| logging_silent           | 105 ns                                                                | 107 ns: 1.01x slower                                               |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                               |
| asyncio_tcp              | 481 ms                                                                | 490 ms: 1.02x slower                                               |
| scimark_sor              | 128 ms                                                                | 131 ms: 1.02x slower                                               |
| pickle                   | 11.7 us                                                               | 11.9 us: 1.02x slower                                              |
| pprint_safe_repr         | 695 ms                                                                | 710 ms: 1.02x slower                                               |
| nqueens                  | 83.5 ms                                                               | 85.4 ms: 1.02x slower                                              |
| unpickle_list            | 5.15 us                                                               | 5.28 us: 1.03x slower                                              |
| regex_dna                | 221 ms                                                                | 227 ms: 1.03x slower                                               |
| pyflate                  | 435 ms                                                                | 447 ms: 1.03x slower                                               |
| deepcopy_reduce          | 2.75 us                                                               | 2.83 us: 1.03x slower                                              |
| pprint_pformat           | 1.43 sec                                                              | 1.48 sec: 1.04x slower                                             |
| coroutines               | 22.9 ms                                                               | 24.2 ms: 1.06x slower                                              |
| pickle_list              | 4.93 us                                                               | 5.31 us: 1.08x slower                                              |
| regex_effbot             | 3.56 ms                                                               | 3.85 ms: 1.08x slower                                              |
| regex_v8                 | 23.1 ms                                                               | 26.8 ms: 1.16x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (38): pylint, genshi_xml, tomli_loads, sqlglot_normalize, json_dumps, dask, xml_etree_parse, telco, comprehensions, async_tree_io, genshi_text, xml_etree_generate, unpickle_pure_python, hexiom, asyncio_websockets, logging_format, bench_mp_pool, go, logging_simple, pidigits, asyncio_tcp_ssl, async_tree_io_tg, 2to3, richards_super, json, deepcopy_memo, xml_etree_process, coverage, generators, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, pycparser, async_tree_cpu_io_mixed_tg, spectral_norm, async_tree_none, deepcopy, async_tree_cpu_io_mixed
Ignored benchmarks (1) of results/bm-20240618-3.14.0a0-9f741e5-JIT/bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json: docutils

# HPT report

- Reliability score: 87.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x