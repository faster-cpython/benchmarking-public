# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_10000
- machine: linux-x86_64
- commit hash: 398f45a
- commit date: 2024-08-13
- overall geometric mean: 1.01x slower
- HPT reliability: 98.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 301 ms: 1.07x slower                                                      |
| docutils       | 2.99 sec                                                              | 2.82 sec: 1.06x faster                                                    |
| html5lib       | 66.6 ms                                                               | 70.0 ms: 1.05x slower                                                     |
| tornado_http   | 94.2 ms                                                               | 95.6 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg       | 873 ms                                                                | 837 ms: 1.04x faster                                                      |
| async_tree_memoization | 428 ms                                                                | 414 ms: 1.04x faster                                                      |
| async_tree_none        | 331 ms                                                                | 325 ms: 1.02x faster                                                      |
| async_generators       | 456 ms                                                                | 454 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                    |
| asyncio_websockets     | 555 ms                                                                | 559 ms: 1.01x slower                                                      |
| coroutines             | 22.4 ms                                                               | 22.9 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 80.1 ms                                                               | 80.9 ms: 1.01x slower                                                     |
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| float          | 70.4 ms                                                               | 74.6 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                                | 141 ms: 1.02x faster                                                      |
| regex_dna      | 214 ms                                                                | 219 ms: 1.02x slower                                                      |
| regex_v8       | 23.8 ms                                                               | 24.5 ms: 1.03x slower                                                     |
| regex_effbot   | 3.56 ms                                                               | 3.76 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| pickle_pure_python   | 302 us                                                                | 305 us: 1.01x slower                                                      |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.02x slower                                                      |
| tomli_loads          | 1.90 sec                                                              | 1.93 sec: 1.02x slower                                                    |
| xml_etree_parse      | 147 ms                                                                | 154 ms: 1.05x slower                                                      |
| xml_etree_process    | 56.1 ms                                                               | 59.5 ms: 1.06x slower                                                     |
| xml_etree_generate   | 80.3 ms                                                               | 86.1 ms: 1.07x slower                                                     |
| xml_etree_iterparse  | 97.6 ms                                                               | 105 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.12 ms                                                               | 7.14 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 9.65 ms                                                               | 9.73 ms: 1.01x slower                                                     |
| genshi_text    | 25.0 ms                                                               | 25.8 ms: 1.03x slower                                                     |
| genshi_xml     | 56.3 ms                                                               | 61.2 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils                 | 2.99 sec                                                              | 2.82 sec: 1.06x faster                                                    |
| async_tree_io_tg         | 873 ms                                                                | 837 ms: 1.04x faster                                                      |
| async_tree_memoization   | 428 ms                                                                | 414 ms: 1.04x faster                                                      |
| sympy_sum                | 175 ms                                                                | 171 ms: 1.03x faster                                                      |
| regex_compile            | 143 ms                                                                | 141 ms: 1.02x faster                                                      |
| async_tree_none          | 331 ms                                                                | 325 ms: 1.02x faster                                                      |
| sympy_str                | 303 ms                                                                | 297 ms: 1.02x faster                                                      |
| telco                    | 7.92 ms                                                               | 7.81 ms: 1.02x faster                                                     |
| gc_traversal             | 3.81 ms                                                               | 3.75 ms: 1.02x faster                                                     |
| deepcopy_memo            | 27.0 us                                                               | 26.7 us: 1.01x faster                                                     |
| pyflate                  | 440 ms                                                                | 433 ms: 1.01x faster                                                      |
| thrift                   | 790 us                                                                | 779 us: 1.01x faster                                                      |
| deepcopy                 | 265 us                                                                | 261 us: 1.01x faster                                                      |
| pprint_safe_repr         | 763 ms                                                                | 753 ms: 1.01x faster                                                      |
| json                     | 5.37 ms                                                               | 5.31 ms: 1.01x faster                                                     |
| sympy_expand             | 509 ms                                                                | 504 ms: 1.01x faster                                                      |
| deepcopy_reduce          | 2.68 us                                                               | 2.65 us: 1.01x faster                                                     |
| sympy_integrate          | 23.0 ms                                                               | 22.9 ms: 1.01x faster                                                     |
| logging_simple           | 5.60 us                                                               | 5.56 us: 1.01x faster                                                     |
| go                       | 148 ms                                                                | 147 ms: 1.01x faster                                                      |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                     |
| async_generators         | 456 ms                                                                | 454 ms: 1.00x faster                                                      |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.12 ms                                                               | 7.14 ms: 1.00x slower                                                     |
| bench_thread_pool        | 820 us                                                                | 823 us: 1.00x slower                                                      |
| hexiom                   | 6.79 ms                                                               | 6.83 ms: 1.01x slower                                                     |
| pathlib                  | 16.1 ms                                                               | 16.2 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                    |
| logging_format           | 6.10 us                                                               | 6.14 us: 1.01x slower                                                     |
| mako                     | 9.65 ms                                                               | 9.73 ms: 1.01x slower                                                     |
| asyncio_websockets       | 555 ms                                                                | 559 ms: 1.01x slower                                                      |
| coverage                 | 85.1 ms                                                               | 85.8 ms: 1.01x slower                                                     |
| raytrace                 | 268 ms                                                                | 271 ms: 1.01x slower                                                      |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.01x slower                                                      |
| crypto_pyaes             | 65.9 ms                                                               | 66.6 ms: 1.01x slower                                                     |
| pickle_pure_python       | 302 us                                                                | 305 us: 1.01x slower                                                      |
| nbody                    | 80.1 ms                                                               | 80.9 ms: 1.01x slower                                                     |
| comprehensions           | 16.4 us                                                               | 16.6 us: 1.01x slower                                                     |
| typing_runtime_protocols | 170 us                                                                | 172 us: 1.01x slower                                                      |
| richards_super           | 45.8 ms                                                               | 46.3 ms: 1.01x slower                                                     |
| scimark_fft              | 307 ms                                                                | 311 ms: 1.01x slower                                                      |
| pidigits                 | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| scimark_sor              | 115 ms                                                                | 117 ms: 1.01x slower                                                      |
| scimark_lu               | 108 ms                                                                | 110 ms: 1.01x slower                                                      |
| tornado_http             | 94.2 ms                                                               | 95.6 ms: 1.02x slower                                                     |
| unpickle_pure_python     | 212 us                                                                | 215 us: 1.02x slower                                                      |
| tomli_loads              | 1.90 sec                                                              | 1.93 sec: 1.02x slower                                                    |
| nqueens                  | 84.1 ms                                                               | 85.9 ms: 1.02x slower                                                     |
| regex_dna                | 214 ms                                                                | 219 ms: 1.02x slower                                                      |
| coroutines               | 22.4 ms                                                               | 22.9 ms: 1.02x slower                                                     |
| spectral_norm            | 98.2 ms                                                               | 101 ms: 1.03x slower                                                      |
| regex_v8                 | 23.8 ms                                                               | 24.5 ms: 1.03x slower                                                     |
| pycparser                | 1.15 sec                                                              | 1.19 sec: 1.03x slower                                                    |
| genshi_text              | 25.0 ms                                                               | 25.8 ms: 1.03x slower                                                     |
| richards                 | 39.6 ms                                                               | 41.1 ms: 1.04x slower                                                     |
| sqlglot_optimize         | 58.4 ms                                                               | 61.0 ms: 1.04x slower                                                     |
| xml_etree_parse          | 147 ms                                                                | 154 ms: 1.05x slower                                                      |
| html5lib                 | 66.6 ms                                                               | 70.0 ms: 1.05x slower                                                     |
| generators               | 33.5 ms                                                               | 35.2 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult  | 4.27 ms                                                               | 4.49 ms: 1.05x slower                                                     |
| regex_effbot             | 3.56 ms                                                               | 3.76 ms: 1.06x slower                                                     |
| float                    | 70.4 ms                                                               | 74.6 ms: 1.06x slower                                                     |
| sqlglot_parse            | 1.32 ms                                                               | 1.40 ms: 1.06x slower                                                     |
| xml_etree_process        | 56.1 ms                                                               | 59.5 ms: 1.06x slower                                                     |
| sqlglot_transpile        | 1.68 ms                                                               | 1.80 ms: 1.07x slower                                                     |
| xml_etree_generate       | 80.3 ms                                                               | 86.1 ms: 1.07x slower                                                     |
| 2to3                     | 281 ms                                                                | 301 ms: 1.07x slower                                                      |
| xml_etree_iterparse      | 97.6 ms                                                               | 105 ms: 1.07x slower                                                      |
| deltablue                | 3.12 ms                                                               | 3.37 ms: 1.08x slower                                                     |
| bpe_tokeniser            | 4.56 sec                                                              | 4.95 sec: 1.08x slower                                                    |
| genshi_xml               | 56.3 ms                                                               | 61.2 ms: 1.09x slower                                                     |
| mdp                      | 2.53 sec                                                              | 2.77 sec: 1.09x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (16): async_tree_io, async_tree_none_tg, pylint, async_tree_cpu_io_mixed, logging_silent, chaos, django_template, asyncio_tcp, sqlglot_normalize, bench_mp_pool, json_loads, pprint_pformat, scimark_monte_carlo, fannkuch, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 98.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x