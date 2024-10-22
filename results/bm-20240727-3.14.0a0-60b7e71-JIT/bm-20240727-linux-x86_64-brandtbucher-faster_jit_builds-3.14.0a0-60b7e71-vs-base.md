# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.90 sec                                                              | 2.91 sec: 1.00x slower                                                   |
| html5lib       | 64.7 ms                                                               | 65.8 ms: 1.02x slower                                                    |
| tornado_http   | 92.9 ms                                                               | 93.3 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators | 456 ms                                                                | 452 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                   |
| async_tree_none  | 324 ms                                                                | 328 ms: 1.01x slower                                                     |
| coroutines       | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                    |
| asyncio_tcp      | 487 ms                                                                | 498 ms: 1.02x slower                                                     |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 70.9 ms                                                               | 70.6 ms: 1.00x faster                                                    |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 134 ms: 1.01x slower                                                     |
| regex_dna      | 226 ms                                                                | 229 ms: 1.02x slower                                                     |
| regex_effbot   | 3.68 ms                                                               | 3.82 ms: 1.04x slower                                                    |
| regex_v8       | 24.5 ms                                                               | 25.8 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 216 us: 1.00x slower                                                     |
| xml_etree_process    | 56.5 ms                                                               | 56.8 ms: 1.01x slower                                                    |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                    |
| xml_etree_generate   | 80.6 ms                                                               | 81.3 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 98.7 ms                                                               | 100 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (4): pickle_pure_python, json_loads, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.22 ms                                                               | 7.17 ms: 1.01x faster                                                    |
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.67 ms                                                               | 9.82 ms: 1.02x slower                                                    |
| genshi_xml     | 56.7 ms                                                               | 58.4 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                      | 2.67 sec                                                              | 2.60 sec: 1.03x faster                                                   |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                    |
| telco                    | 7.94 ms                                                               | 7.84 ms: 1.01x faster                                                    |
| async_generators         | 456 ms                                                                | 452 ms: 1.01x faster                                                     |
| python_startup_no_site   | 7.22 ms                                                               | 7.17 ms: 1.01x faster                                                    |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                    |
| bpe_tokeniser            | 4.53 sec                                                              | 4.50 sec: 1.01x faster                                                   |
| crypto_pyaes             | 66.7 ms                                                               | 66.3 ms: 1.01x faster                                                    |
| spectral_norm            | 101 ms                                                                | 101 ms: 1.01x faster                                                     |
| float                    | 70.9 ms                                                               | 70.6 ms: 1.00x faster                                                    |
| create_gc_cycles         | 1.77 ms                                                               | 1.77 ms: 1.00x faster                                                    |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                   |
| hexiom                   | 6.57 ms                                                               | 6.59 ms: 1.00x slower                                                    |
| tornado_http             | 92.9 ms                                                               | 93.3 ms: 1.00x slower                                                    |
| richards_super           | 46.7 ms                                                               | 46.9 ms: 1.00x slower                                                    |
| docutils                 | 2.90 sec                                                              | 2.91 sec: 1.00x slower                                                   |
| unpickle_pure_python     | 215 us                                                                | 216 us: 1.00x slower                                                     |
| xml_etree_process        | 56.5 ms                                                               | 56.8 ms: 1.01x slower                                                    |
| deepcopy                 | 271 us                                                                | 273 us: 1.01x slower                                                     |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                    |
| sqlglot_transpile        | 1.59 ms                                                               | 1.60 ms: 1.01x slower                                                    |
| nqueens                  | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                    |
| xml_etree_generate       | 80.6 ms                                                               | 81.3 ms: 1.01x slower                                                    |
| typing_runtime_protocols | 168 us                                                                | 169 us: 1.01x slower                                                     |
| regex_compile            | 133 ms                                                                | 134 ms: 1.01x slower                                                     |
| async_tree_none          | 324 ms                                                                | 328 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.26 ms                                                               | 1.28 ms: 1.01x slower                                                    |
| json                     | 5.10 ms                                                               | 5.17 ms: 1.01x slower                                                    |
| coverage                 | 91.7 ms                                                               | 93.0 ms: 1.01x slower                                                    |
| gc_traversal             | 3.73 ms                                                               | 3.78 ms: 1.01x slower                                                    |
| chaos                    | 57.7 ms                                                               | 58.5 ms: 1.01x slower                                                    |
| regex_dna                | 226 ms                                                                | 229 ms: 1.02x slower                                                     |
| xml_etree_iterparse      | 98.7 ms                                                               | 100 ms: 1.02x slower                                                     |
| mako                     | 9.67 ms                                                               | 9.82 ms: 1.02x slower                                                    |
| sqlglot_normalize        | 113 ms                                                                | 114 ms: 1.02x slower                                                     |
| raytrace                 | 266 ms                                                                | 270 ms: 1.02x slower                                                     |
| html5lib                 | 64.7 ms                                                               | 65.8 ms: 1.02x slower                                                    |
| coroutines               | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                    |
| logging_silent           | 101 ns                                                                | 103 ns: 1.02x slower                                                     |
| deepcopy_reduce          | 2.75 us                                                               | 2.81 us: 1.02x slower                                                    |
| asyncio_tcp              | 487 ms                                                                | 498 ms: 1.02x slower                                                     |
| scimark_fft              | 307 ms                                                                | 316 ms: 1.03x slower                                                     |
| thrift                   | 778 us                                                                | 800 us: 1.03x slower                                                     |
| scimark_lu               | 125 ms                                                                | 128 ms: 1.03x slower                                                     |
| scimark_sor              | 126 ms                                                                | 130 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult  | 4.17 ms                                                               | 4.30 ms: 1.03x slower                                                    |
| genshi_xml               | 56.7 ms                                                               | 58.4 ms: 1.03x slower                                                    |
| scimark_monte_carlo      | 59.8 ms                                                               | 61.8 ms: 1.03x slower                                                    |
| regex_effbot             | 3.68 ms                                                               | 3.82 ms: 1.04x slower                                                    |
| go                       | 143 ms                                                                | 149 ms: 1.04x slower                                                     |
| deltablue                | 3.50 ms                                                               | 3.65 ms: 1.04x slower                                                    |
| regex_v8                 | 24.5 ms                                                               | 25.8 ms: 1.05x slower                                                    |
| pycparser                | 1.12 sec                                                              | 1.18 sec: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (36): deepcopy_memo, logging_simple, logging_format, sympy_integrate, richards, meteor_contest, pprint_safe_repr, pickle_pure_python, bench_mp_pool, asyncio_websockets, sympy_expand, sympy_str, 2to3, pathlib, json_loads, sqlglot_optimize, dask, pprint_pformat, generators, sympy_sum, bench_thread_pool, fannkuch, async_tree_cpu_io_mixed_tg, django_template, pylint, async_tree_cpu_io_mixed, tomli_loads, pyflate, genshi_text, xml_etree_parse, async_tree_memoization_tg, nbody, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x