# Results vs. base

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.00x faster
- HPT reliability: 66.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                                                               | 281 ms: 1.02x slower                                                                                     |
| chameleon      | 7.22 ms                                                                                              | 7.11 ms: 1.02x faster                                                                                    |
| docutils       | 2.83 sec                                                                                             | 2.99 sec: 1.06x slower                                                                                   |
| html5lib       | 67.2 ms                                                                                              | 69.1 ms: 1.03x slower                                                                                    |
| tornado_http   | 94.6 ms                                                                                              | 96.9 ms: 1.02x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                                                              | 73.0 ms: 1.08x faster                                                                                    |
| nbody          | 88.3 ms                                                                                              | 83.5 ms: 1.06x faster                                                                                    |
| pidigits       | 191 ms                                                                                               | 188 ms: 1.02x faster                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.05x faster                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                                                              | 25.2 ms: 1.01x slower                                                                                    |
| regex_effbot   | 3.67 ms                                                                                              | 3.69 ms: 1.01x slower                                                                                    |
| regex_compile  | 137 ms                                                                                               | 138 ms: 1.01x slower                                                                                     |
| regex_dna      | 221 ms                                                                                               | 230 ms: 1.04x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                                                             | 1.95 sec: 1.09x faster                                                                                   |
| xml_etree_parse      | 162 ms                                                                                               | 149 ms: 1.09x faster                                                                                     |
| xml_etree_iterparse  | 107 ms                                                                                               | 102 ms: 1.06x faster                                                                                     |
| xml_etree_generate   | 87.4 ms                                                                                              | 82.9 ms: 1.06x faster                                                                                    |
| xml_etree_process    | 61.2 ms                                                                                              | 58.5 ms: 1.05x faster                                                                                    |
| json_dumps           | 10.7 ms                                                                                              | 10.3 ms: 1.04x faster                                                                                    |
| pickle_pure_python   | 305 us                                                                                               | 300 us: 1.02x faster                                                                                     |
| unpickle_list        | 5.34 us                                                                                              | 5.26 us: 1.01x faster                                                                                    |
| pickle_list          | 5.11 us                                                                                              | 5.08 us: 1.00x faster                                                                                    |
| unpickle_pure_python | 218 us                                                                                               | 222 us: 1.02x slower                                                                                     |
| pickle               | 11.5 us                                                                                              | 11.9 us: 1.03x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                | 1.02x faster                                                                                             |

Benchmark hidden because not significant (3): json_loads, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                                                              | 11.3 ms: 1.05x slower                                                                                    |
| python_startup_no_site | 7.11 ms                                                                                              | 7.62 ms: 1.07x slower                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.06x slower                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                                              | 9.83 ms: 1.14x faster                                                                                    |
| django_template | 34.8 ms                                                                                              | 36.4 ms: 1.05x slower                                                                                    |
| genshi_text     | 23.7 ms                                                                                              | 25.5 ms: 1.08x slower                                                                                    |
| genshi_xml      | 51.6 ms                                                                                              | 60.2 ms: 1.17x slower                                                                                    |
| Geometric mean  | (ref)                                                                                                | 1.03x slower                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                                                               | 317 ms: 1.24x faster                                                                                     |
| richards                 | 50.9 ms                                                                                              | 41.7 ms: 1.22x faster                                                                                    |
| richards_super           | 57.4 ms                                                                                              | 48.4 ms: 1.19x faster                                                                                    |
| scimark_sparse_mat_mult  | 5.27 ms                                                                                              | 4.48 ms: 1.18x faster                                                                                    |
| mako                     | 11.2 ms                                                                                              | 9.83 ms: 1.14x faster                                                                                    |
| crypto_pyaes             | 77.5 ms                                                                                              | 68.0 ms: 1.14x faster                                                                                    |
| spectral_norm            | 116 ms                                                                                               | 102 ms: 1.14x faster                                                                                     |
| fannkuch                 | 402 ms                                                                                               | 358 ms: 1.12x faster                                                                                     |
| pyflate                  | 484 ms                                                                                               | 436 ms: 1.11x faster                                                                                     |
| scimark_monte_carlo      | 69.2 ms                                                                                              | 62.7 ms: 1.10x faster                                                                                    |
| tomli_loads              | 2.12 sec                                                                                             | 1.95 sec: 1.09x faster                                                                                   |
| xml_etree_parse          | 162 ms                                                                                               | 149 ms: 1.09x faster                                                                                     |
| float                    | 78.9 ms                                                                                              | 73.0 ms: 1.08x faster                                                                                    |
| pprint_pformat           | 1.56 sec                                                                                             | 1.45 sec: 1.07x faster                                                                                   |
| deepcopy_memo            | 39.7 us                                                                                              | 37.3 us: 1.06x faster                                                                                    |
| mdp                      | 2.79 sec                                                                                             | 2.62 sec: 1.06x faster                                                                                   |
| pprint_safe_repr         | 758 ms                                                                                               | 715 ms: 1.06x faster                                                                                     |
| nbody                    | 88.3 ms                                                                                              | 83.5 ms: 1.06x faster                                                                                    |
| xml_etree_iterparse      | 107 ms                                                                                               | 102 ms: 1.06x faster                                                                                     |
| xml_etree_generate       | 87.4 ms                                                                                              | 82.9 ms: 1.06x faster                                                                                    |
| chaos                    | 61.3 ms                                                                                              | 58.5 ms: 1.05x faster                                                                                    |
| xml_etree_process        | 61.2 ms                                                                                              | 58.5 ms: 1.05x faster                                                                                    |
| sqlite_synth             | 2.99 us                                                                                              | 2.88 us: 1.04x faster                                                                                    |
| json_dumps               | 10.7 ms                                                                                              | 10.3 ms: 1.04x faster                                                                                    |
| telco                    | 8.41 ms                                                                                              | 8.12 ms: 1.04x faster                                                                                    |
| bpe_tokeniser            | 5.02 sec                                                                                             | 4.88 sec: 1.03x faster                                                                                   |
| coroutines               | 23.2 ms                                                                                              | 22.6 ms: 1.03x faster                                                                                    |
| logging_format           | 6.47 us                                                                                              | 6.30 us: 1.03x faster                                                                                    |
| gc_traversal             | 3.98 ms                                                                                              | 3.88 ms: 1.02x faster                                                                                    |
| pickle_pure_python       | 305 us                                                                                               | 300 us: 1.02x faster                                                                                     |
| sqlglot_parse            | 1.32 ms                                                                                              | 1.30 ms: 1.02x faster                                                                                    |
| pidigits                 | 191 ms                                                                                               | 188 ms: 1.02x faster                                                                                     |
| chameleon                | 7.22 ms                                                                                              | 7.11 ms: 1.02x faster                                                                                    |
| unpickle_list            | 5.34 us                                                                                              | 5.26 us: 1.01x faster                                                                                    |
| deepcopy_reduce          | 3.35 us                                                                                              | 3.30 us: 1.01x faster                                                                                    |
| logging_simple           | 5.74 us                                                                                              | 5.70 us: 1.01x faster                                                                                    |
| pickle_list              | 5.11 us                                                                                              | 5.08 us: 1.00x faster                                                                                    |
| sqlglot_transpile        | 1.63 ms                                                                                              | 1.63 ms: 1.00x faster                                                                                    |
| scimark_sor              | 127 ms                                                                                               | 128 ms: 1.00x slower                                                                                     |
| regex_v8                 | 25.1 ms                                                                                              | 25.2 ms: 1.01x slower                                                                                    |
| regex_effbot             | 3.67 ms                                                                                              | 3.69 ms: 1.01x slower                                                                                    |
| comprehensions           | 16.6 us                                                                                              | 16.7 us: 1.01x slower                                                                                    |
| pathlib                  | 17.3 ms                                                                                              | 17.4 ms: 1.01x slower                                                                                    |
| asyncio_tcp_ssl          | 1.84 sec                                                                                             | 1.86 sec: 1.01x slower                                                                                   |
| create_gc_cycles         | 1.82 ms                                                                                              | 1.83 ms: 1.01x slower                                                                                    |
| meteor_contest           | 110 ms                                                                                               | 111 ms: 1.01x slower                                                                                     |
| regex_compile            | 137 ms                                                                                               | 138 ms: 1.01x slower                                                                                     |
| unpickle_pure_python     | 218 us                                                                                               | 222 us: 1.02x slower                                                                                     |
| deepcopy                 | 367 us                                                                                               | 375 us: 1.02x slower                                                                                     |
| dask                     | 369 ms                                                                                               | 377 ms: 1.02x slower                                                                                     |
| sqlglot_optimize         | 55.5 ms                                                                                              | 56.8 ms: 1.02x slower                                                                                    |
| tornado_http             | 94.6 ms                                                                                              | 96.9 ms: 1.02x slower                                                                                    |
| 2to3                     | 274 ms                                                                                               | 281 ms: 1.02x slower                                                                                     |
| logging_silent           | 105 ns                                                                                               | 108 ns: 1.03x slower                                                                                     |
| asyncio_tcp              | 508 ms                                                                                               | 522 ms: 1.03x slower                                                                                     |
| html5lib                 | 67.2 ms                                                                                              | 69.1 ms: 1.03x slower                                                                                    |
| flaskblogging            | 9.01 ms                                                                                              | 9.27 ms: 1.03x slower                                                                                    |
| sqlglot_normalize        | 110 ms                                                                                               | 114 ms: 1.03x slower                                                                                     |
| pickle                   | 11.5 us                                                                                              | 11.9 us: 1.03x slower                                                                                    |
| regex_dna                | 221 ms                                                                                               | 230 ms: 1.04x slower                                                                                     |
| dulwich_log              | 67.2 ms                                                                                              | 69.7 ms: 1.04x slower                                                                                    |
| bench_thread_pool        | 834 us                                                                                               | 867 us: 1.04x slower                                                                                     |
| djangocms                | 31.5 us                                                                                              | 32.8 us: 1.04x slower                                                                                    |
| go                       | 145 ms                                                                                               | 151 ms: 1.04x slower                                                                                     |
| django_template          | 34.8 ms                                                                                              | 36.4 ms: 1.05x slower                                                                                    |
| async_generators         | 442 ms                                                                                               | 462 ms: 1.05x slower                                                                                     |
| python_startup           | 10.8 ms                                                                                              | 11.3 ms: 1.05x slower                                                                                    |
| scimark_lu               | 122 ms                                                                                               | 127 ms: 1.05x slower                                                                                     |
| raytrace                 | 267 ms                                                                                               | 280 ms: 1.05x slower                                                                                     |
| typing_runtime_protocols | 165 us                                                                                               | 173 us: 1.05x slower                                                                                     |
| gunicorn                 | 1.28 ms                                                                                              | 1.34 ms: 1.05x slower                                                                                    |
| docutils                 | 2.83 sec                                                                                             | 2.99 sec: 1.06x slower                                                                                   |
| aiohttp                  | 1.18 ms                                                                                              | 1.25 ms: 1.06x slower                                                                                    |
| hexiom                   | 6.30 ms                                                                                              | 6.67 ms: 1.06x slower                                                                                    |
| nqueens                  | 81.4 ms                                                                                              | 86.5 ms: 1.06x slower                                                                                    |
| sympy_str                | 282 ms                                                                                               | 302 ms: 1.07x slower                                                                                     |
| python_startup_no_site   | 7.11 ms                                                                                              | 7.62 ms: 1.07x slower                                                                                    |
| genshi_text              | 23.7 ms                                                                                              | 25.5 ms: 1.08x slower                                                                                    |
| sympy_expand             | 473 ms                                                                                               | 510 ms: 1.08x slower                                                                                     |
| mypy2                    | 742 ms                                                                                               | 814 ms: 1.10x slower                                                                                     |
| sympy_integrate          | 20.5 ms                                                                                              | 22.5 ms: 1.10x slower                                                                                    |
| sympy_sum                | 156 ms                                                                                               | 172 ms: 1.10x slower                                                                                     |
| pylint                   | 317 ms                                                                                               | 353 ms: 1.11x slower                                                                                     |
| generators               | 29.6 ms                                                                                              | 33.5 ms: 1.13x slower                                                                                    |
| deltablue                | 3.25 ms                                                                                              | 3.70 ms: 1.14x slower                                                                                    |
| genshi_xml               | 51.6 ms                                                                                              | 60.2 ms: 1.17x slower                                                                                    |
| Geometric mean           | (ref)                                                                                                | 1.00x faster                                                                                             |

Benchmark hidden because not significant (17): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, coverage, async_tree_none, json_loads, unpickle, asyncio_websockets, pickle_dict, bench_mp_pool, async_tree_cpu_io_mixed, thrift, json, pycparser, async_tree_io_tg

# HPT report

- Reliability score: 66.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x