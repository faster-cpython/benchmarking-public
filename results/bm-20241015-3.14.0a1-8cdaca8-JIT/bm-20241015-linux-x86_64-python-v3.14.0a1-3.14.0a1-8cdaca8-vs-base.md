# Results vs. base

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.013x slower
- HPT reliability: 83.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                                               | 277 ms: 1.09x slower                                                                                     |
| docutils       | 2.65 sec                                                                                             | 2.91 sec: 1.10x slower                                                                                   |
| html5lib       | 61.9 ms                                                                                              | 63.7 ms: 1.03x slower                                                                                    |
| sphinx         | 1.04 sec                                                                                             | 1.18 sec: 1.13x slower                                                                                   |
| tornado_http   | 89.9 ms                                                                                              | 94.3 ms: 1.05x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.08x slower                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|--------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg   | 968 ms                                                                                               | 966 ms: 1.00x faster                                                                                     |
| asyncio_websockets | 554 ms                                                                                               | 558 ms: 1.01x slower                                                                                     |
| coroutines         | 23.1 ms                                                                                              | 23.3 ms: 1.01x slower                                                                                    |
| async_tree_none    | 326 ms                                                                                               | 331 ms: 1.01x slower                                                                                     |
| asyncio_tcp_ssl    | 1.79 sec                                                                                             | 1.82 sec: 1.02x slower                                                                                   |
| asyncio_tcp        | 486 ms                                                                                               | 501 ms: 1.03x slower                                                                                     |
| async_generators   | 447 ms                                                                                               | 478 ms: 1.07x slower                                                                                     |
| Geometric mean     | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| nbody          | 88.8 ms                                                                                              | 81.3 ms: 1.09x faster                                                                                    |
| float          | 79.2 ms                                                                                              | 75.4 ms: 1.05x faster                                                                                    |
| pidigits       | 188 ms                                                                                               | 186 ms: 1.01x faster                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.05x faster                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                                               | 217 ms: 1.02x slower                                                                                     |
| regex_effbot   | 3.60 ms                                                                                              | 3.67 ms: 1.02x slower                                                                                    |
| regex_v8       | 25.5 ms                                                                                              | 26.4 ms: 1.03x slower                                                                                    |
| regex_compile  | 129 ms                                                                                               | 140 ms: 1.09x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.04x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|---------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| xml_etree_generate  | 87.5 ms                                                                                              | 78.6 ms: 1.11x faster                                                                                    |
| xml_etree_process   | 60.5 ms                                                                                              | 55.5 ms: 1.09x faster                                                                                    |
| tomli_loads         | 2.09 sec                                                                                             | 1.92 sec: 1.09x faster                                                                                   |
| xml_etree_parse     | 157 ms                                                                                               | 148 ms: 1.06x faster                                                                                     |
| xml_etree_iterparse | 104 ms                                                                                               | 99.9 ms: 1.04x faster                                                                                    |
| json_dumps          | 11.1 ms                                                                                              | 10.8 ms: 1.02x faster                                                                                    |
| pickle_pure_python  | 313 us                                                                                               | 310 us: 1.01x faster                                                                                     |
| unpickle_list       | 5.49 us                                                                                              | 5.59 us: 1.02x slower                                                                                    |
| pickle_list         | 5.10 us                                                                                              | 5.20 us: 1.02x slower                                                                                    |
| pickle              | 11.5 us                                                                                              | 12.0 us: 1.04x slower                                                                                    |
| pickle_dict         | 33.3 us                                                                                              | 35.8 us: 1.08x slower                                                                                    |
| Geometric mean      | (ref)                                                                                                | 1.02x faster                                                                                             |

Benchmark hidden because not significant (3): unpickle, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup         | 11.8 ms                                                                                              | 11.9 ms: 1.01x slower                                                                                    |
| python_startup_no_site | 7.02 ms                                                                                              | 7.10 ms: 1.01x slower                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                                              | 10.1 ms: 1.12x faster                                                                                    |
| genshi_text     | 23.4 ms                                                                                              | 25.2 ms: 1.07x slower                                                                                    |
| django_template | 34.0 ms                                                                                              | 37.2 ms: 1.09x slower                                                                                    |
| genshi_xml      | 52.1 ms                                                                                              | 58.9 ms: 1.13x slower                                                                                    |
| Geometric mean  | (ref)                                                                                                | 1.04x slower                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 360 ms                                                                                               | 319 ms: 1.13x faster                                                                                     |
| richards                 | 46.0 ms                                                                                              | 41.0 ms: 1.12x faster                                                                                    |
| mako                     | 11.2 ms                                                                                              | 10.1 ms: 1.12x faster                                                                                    |
| xml_etree_generate       | 87.5 ms                                                                                              | 78.6 ms: 1.11x faster                                                                                    |
| richards_super           | 52.8 ms                                                                                              | 48.0 ms: 1.10x faster                                                                                    |
| nbody                    | 88.8 ms                                                                                              | 81.3 ms: 1.09x faster                                                                                    |
| xml_etree_process        | 60.5 ms                                                                                              | 55.5 ms: 1.09x faster                                                                                    |
| tomli_loads              | 2.09 sec                                                                                             | 1.92 sec: 1.09x faster                                                                                   |
| bpe_tokeniser            | 4.80 sec                                                                                             | 4.44 sec: 1.08x faster                                                                                   |
| fannkuch                 | 404 ms                                                                                               | 377 ms: 1.07x faster                                                                                     |
| crypto_pyaes             | 72.1 ms                                                                                              | 67.5 ms: 1.07x faster                                                                                    |
| xml_etree_parse          | 157 ms                                                                                               | 148 ms: 1.06x faster                                                                                     |
| scimark_sor              | 125 ms                                                                                               | 118 ms: 1.06x faster                                                                                     |
| pyflate                  | 471 ms                                                                                               | 446 ms: 1.06x faster                                                                                     |
| float                    | 79.2 ms                                                                                              | 75.4 ms: 1.05x faster                                                                                    |
| scimark_monte_carlo      | 67.4 ms                                                                                              | 64.1 ms: 1.05x faster                                                                                    |
| mdp                      | 2.67 sec                                                                                             | 2.56 sec: 1.04x faster                                                                                   |
| xml_etree_iterparse      | 104 ms                                                                                               | 99.9 ms: 1.04x faster                                                                                    |
| telco                    | 7.97 ms                                                                                              | 7.68 ms: 1.04x faster                                                                                    |
| deepcopy_memo            | 30.4 us                                                                                              | 29.4 us: 1.03x faster                                                                                    |
| gc_traversal             | 4.54 ms                                                                                              | 4.40 ms: 1.03x faster                                                                                    |
| pprint_pformat           | 1.51 sec                                                                                             | 1.46 sec: 1.03x faster                                                                                   |
| json_dumps               | 11.1 ms                                                                                              | 10.8 ms: 1.02x faster                                                                                    |
| logging_silent           | 100 ns                                                                                               | 98.0 ns: 1.02x faster                                                                                    |
| chaos                    | 60.1 ms                                                                                              | 59.1 ms: 1.02x faster                                                                                    |
| json                     | 5.03 ms                                                                                              | 4.95 ms: 1.02x faster                                                                                    |
| scimark_sparse_mat_mult  | 4.79 ms                                                                                              | 4.72 ms: 1.02x faster                                                                                    |
| pprint_safe_repr         | 734 ms                                                                                               | 726 ms: 1.01x faster                                                                                     |
| pickle_pure_python       | 313 us                                                                                               | 310 us: 1.01x faster                                                                                     |
| pidigits                 | 188 ms                                                                                               | 186 ms: 1.01x faster                                                                                     |
| async_tree_io_tg         | 968 ms                                                                                               | 966 ms: 1.00x faster                                                                                     |
| create_gc_cycles         | 2.67 ms                                                                                              | 2.67 ms: 1.00x slower                                                                                    |
| meteor_contest           | 107 ms                                                                                               | 108 ms: 1.01x slower                                                                                     |
| pathlib                  | 16.1 ms                                                                                              | 16.2 ms: 1.01x slower                                                                                    |
| typing_runtime_protocols | 161 us                                                                                               | 162 us: 1.01x slower                                                                                     |
| asyncio_websockets       | 554 ms                                                                                               | 558 ms: 1.01x slower                                                                                     |
| coroutines               | 23.1 ms                                                                                              | 23.3 ms: 1.01x slower                                                                                    |
| python_startup           | 11.8 ms                                                                                              | 11.9 ms: 1.01x slower                                                                                    |
| scimark_lu               | 113 ms                                                                                               | 114 ms: 1.01x slower                                                                                     |
| python_startup_no_site   | 7.02 ms                                                                                              | 7.10 ms: 1.01x slower                                                                                    |
| coverage                 | 83.6 ms                                                                                              | 84.6 ms: 1.01x slower                                                                                    |
| async_tree_none          | 326 ms                                                                                               | 331 ms: 1.01x slower                                                                                     |
| regex_dna                | 214 ms                                                                                               | 217 ms: 1.02x slower                                                                                     |
| unpickle_list            | 5.49 us                                                                                              | 5.59 us: 1.02x slower                                                                                    |
| asyncio_tcp_ssl          | 1.79 sec                                                                                             | 1.82 sec: 1.02x slower                                                                                   |
| pickle_list              | 5.10 us                                                                                              | 5.20 us: 1.02x slower                                                                                    |
| comprehensions           | 16.7 us                                                                                              | 17.0 us: 1.02x slower                                                                                    |
| thrift                   | 773 us                                                                                               | 787 us: 1.02x slower                                                                                     |
| regex_effbot             | 3.60 ms                                                                                              | 3.67 ms: 1.02x slower                                                                                    |
| logging_simple           | 5.52 us                                                                                              | 5.63 us: 1.02x slower                                                                                    |
| deltablue                | 3.23 ms                                                                                              | 3.29 ms: 1.02x slower                                                                                    |
| deepcopy_reduce          | 2.69 us                                                                                              | 2.75 us: 1.02x slower                                                                                    |
| html5lib                 | 61.9 ms                                                                                              | 63.7 ms: 1.03x slower                                                                                    |
| asyncio_tcp              | 486 ms                                                                                               | 501 ms: 1.03x slower                                                                                     |
| sqlglot_parse            | 1.29 ms                                                                                              | 1.33 ms: 1.03x slower                                                                                    |
| regex_v8                 | 25.5 ms                                                                                              | 26.4 ms: 1.03x slower                                                                                    |
| deepcopy                 | 264 us                                                                                               | 273 us: 1.03x slower                                                                                     |
| pickle                   | 11.5 us                                                                                              | 12.0 us: 1.04x slower                                                                                    |
| dulwich_log              | 63.5 ms                                                                                              | 66.5 ms: 1.05x slower                                                                                    |
| bench_thread_pool        | 837 us                                                                                               | 877 us: 1.05x slower                                                                                     |
| tornado_http             | 89.9 ms                                                                                              | 94.3 ms: 1.05x slower                                                                                    |
| raytrace                 | 262 ms                                                                                               | 276 ms: 1.05x slower                                                                                     |
| sqlglot_transpile        | 1.59 ms                                                                                              | 1.69 ms: 1.06x slower                                                                                    |
| async_generators         | 447 ms                                                                                               | 478 ms: 1.07x slower                                                                                     |
| pycparser                | 1.12 sec                                                                                             | 1.20 sec: 1.07x slower                                                                                   |
| genshi_text              | 23.4 ms                                                                                              | 25.2 ms: 1.07x slower                                                                                    |
| pickle_dict              | 33.3 us                                                                                              | 35.8 us: 1.08x slower                                                                                    |
| bench_mp_pool            | 77.9 ms                                                                                              | 84.2 ms: 1.08x slower                                                                                    |
| sqlglot_normalize        | 106 ms                                                                                               | 115 ms: 1.08x slower                                                                                     |
| nqueens                  | 79.9 ms                                                                                              | 86.7 ms: 1.08x slower                                                                                    |
| regex_compile            | 129 ms                                                                                               | 140 ms: 1.09x slower                                                                                     |
| 2to3                     | 254 ms                                                                                               | 277 ms: 1.09x slower                                                                                     |
| django_template          | 34.0 ms                                                                                              | 37.2 ms: 1.09x slower                                                                                    |
| docutils                 | 2.65 sec                                                                                             | 2.91 sec: 1.10x slower                                                                                   |
| go                       | 120 ms                                                                                               | 133 ms: 1.11x slower                                                                                     |
| sympy_expand             | 450 ms                                                                                               | 502 ms: 1.11x slower                                                                                     |
| genshi_xml               | 52.1 ms                                                                                              | 58.9 ms: 1.13x slower                                                                                    |
| sphinx                   | 1.04 sec                                                                                             | 1.18 sec: 1.13x slower                                                                                   |
| sqlglot_optimize         | 53.2 ms                                                                                              | 60.2 ms: 1.13x slower                                                                                    |
| hexiom                   | 6.19 ms                                                                                              | 7.03 ms: 1.14x slower                                                                                    |
| sympy_str                | 266 ms                                                                                               | 303 ms: 1.14x slower                                                                                     |
| pylint                   | 317 ms                                                                                               | 376 ms: 1.18x slower                                                                                     |
| sympy_integrate          | 19.8 ms                                                                                              | 23.6 ms: 1.19x slower                                                                                    |
| sympy_sum                | 146 ms                                                                                               | 176 ms: 1.21x slower                                                                                     |
| generators               | 27.0 ms                                                                                              | 35.4 ms: 1.31x slower                                                                                    |
| unpack_sequence          | 48.5 ns                                                                                              | 110 ns: 2.27x slower                                                                                     |
| Geometric mean           | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmark hidden because not significant (12): unpickle, async_tree_none_tg, async_tree_cpu_io_mixed_tg, sqlite_synth, json_loads, unpickle_pure_python, async_tree_memoization_tg, logging_format, async_tree_cpu_io_mixed, spectral_norm, async_tree_memoization, async_tree_io

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 83.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x