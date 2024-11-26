# Results vs. base

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.006x slower
- HPT reliability: 79.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                                                                | 310 ms: 1.10x slower                                                                                                      |
| docutils       | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| html5lib       | 72.4 ms                                                                                                               | 70.3 ms: 1.03x faster                                                                                                     |
| tornado_http   | 117 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|--------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines         | 22.0 ms                                                                                                               | 21.4 ms: 1.03x faster                                                                                                     |
| asyncio_websockets | 397 ms                                                                                                                | 391 ms: 1.01x faster                                                                                                      |
| asyncio_tcp        | 372 ms                                                                                                                | 376 ms: 1.01x slower                                                                                                      |
| asyncio_tcp_ssl    | 1.57 sec                                                                                                              | 1.60 sec: 1.02x slower                                                                                                    |
| async_generators   | 359 ms                                                                                                                | 380 ms: 1.06x slower                                                                                                      |
| Geometric mean     | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (8): async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 91.6 ms                                                                                                               | 81.1 ms: 1.13x faster                                                                                                     |
| float          | 78.2 ms                                                                                                               | 73.7 ms: 1.06x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.07x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                                                               | 3.46 ms: 1.04x faster                                                                                                     |
| regex_dna      | 245 ms                                                                                                                | 235 ms: 1.04x faster                                                                                                      |
| regex_v8       | 25.2 ms                                                                                                               | 25.3 ms: 1.00x slower                                                                                                     |
| regex_compile  | 142 ms                                                                                                                | 147 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.63 sec                                                                                                              | 2.12 sec: 1.24x faster                                                                                                    |
| xml_etree_generate   | 84.9 ms                                                                                                               | 78.7 ms: 1.08x faster                                                                                                     |
| unpickle_pure_python | 229 us                                                                                                                | 213 us: 1.07x faster                                                                                                      |
| xml_etree_process    | 59.4 ms                                                                                                               | 55.8 ms: 1.07x faster                                                                                                     |
| xml_etree_iterparse  | 100 ms                                                                                                                | 98.3 ms: 1.02x faster                                                                                                     |
| json_loads           | 24.6 us                                                                                                               | 24.7 us: 1.01x slower                                                                                                     |
| unpickle_list        | 4.69 us                                                                                                               | 4.75 us: 1.01x slower                                                                                                     |
| xml_etree_parse      | 141 ms                                                                                                                | 143 ms: 1.02x slower                                                                                                      |
| pickle_pure_python   | 321 us                                                                                                                | 328 us: 1.02x slower                                                                                                      |
| json_dumps           | 10.6 ms                                                                                                               | 10.9 ms: 1.02x slower                                                                                                     |
| unpickle             | 15.1 us                                                                                                               | 15.4 us: 1.02x slower                                                                                                     |
| pickle_list          | 4.28 us                                                                                                               | 4.51 us: 1.05x slower                                                                                                     |
| pickle               | 10.2 us                                                                                                               | 10.8 us: 1.06x slower                                                                                                     |
| pickle_dict          | 30.3 us                                                                                                               | 32.4 us: 1.07x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                                                                               | 8.97 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                                                               | 9.10 ms: 1.14x faster                                                                                                     |
| django_template | 39.5 ms                                                                                                               | 43.1 ms: 1.09x slower                                                                                                     |
| genshi_text     | 25.7 ms                                                                                                               | 28.3 ms: 1.10x slower                                                                                                     |
| genshi_xml      | 56.4 ms                                                                                                               | 62.3 ms: 1.11x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.04x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 2.63 sec                                                                                                              | 2.12 sec: 1.24x faster                                                                                                    |
| spectral_norm            | 96.7 ms                                                                                                               | 82.3 ms: 1.18x faster                                                                                                     |
| scimark_sor              | 120 ms                                                                                                                | 104 ms: 1.15x faster                                                                                                      |
| mako                     | 10.4 ms                                                                                                               | 9.10 ms: 1.14x faster                                                                                                     |
| richards                 | 50.9 ms                                                                                                               | 44.9 ms: 1.14x faster                                                                                                     |
| nbody                    | 91.6 ms                                                                                                               | 81.1 ms: 1.13x faster                                                                                                     |
| deepcopy_memo            | 29.3 us                                                                                                               | 26.9 us: 1.09x faster                                                                                                     |
| xml_etree_generate       | 84.9 ms                                                                                                               | 78.7 ms: 1.08x faster                                                                                                     |
| richards_super           | 57.0 ms                                                                                                               | 52.9 ms: 1.08x faster                                                                                                     |
| scimark_fft              | 305 ms                                                                                                                | 283 ms: 1.08x faster                                                                                                      |
| unpickle_pure_python     | 229 us                                                                                                                | 213 us: 1.07x faster                                                                                                      |
| deltablue                | 3.42 ms                                                                                                               | 3.19 ms: 1.07x faster                                                                                                     |
| xml_etree_process        | 59.4 ms                                                                                                               | 55.8 ms: 1.07x faster                                                                                                     |
| float                    | 78.2 ms                                                                                                               | 73.7 ms: 1.06x faster                                                                                                     |
| regex_effbot             | 3.61 ms                                                                                                               | 3.46 ms: 1.04x faster                                                                                                     |
| create_gc_cycles         | 1.99 ms                                                                                                               | 1.91 ms: 1.04x faster                                                                                                     |
| scimark_sparse_mat_mult  | 4.12 ms                                                                                                               | 3.96 ms: 1.04x faster                                                                                                     |
| regex_dna                | 245 ms                                                                                                                | 235 ms: 1.04x faster                                                                                                      |
| pyflate                  | 483 ms                                                                                                                | 465 ms: 1.04x faster                                                                                                      |
| crypto_pyaes             | 73.2 ms                                                                                                               | 70.6 ms: 1.04x faster                                                                                                     |
| telco                    | 8.34 ms                                                                                                               | 8.05 ms: 1.04x faster                                                                                                     |
| bpe_tokeniser            | 4.94 sec                                                                                                              | 4.78 sec: 1.03x faster                                                                                                    |
| html5lib                 | 72.4 ms                                                                                                               | 70.3 ms: 1.03x faster                                                                                                     |
| dulwich_log              | 66.4 ms                                                                                                               | 64.6 ms: 1.03x faster                                                                                                     |
| scimark_lu               | 99.0 ms                                                                                                               | 96.5 ms: 1.03x faster                                                                                                     |
| coroutines               | 22.0 ms                                                                                                               | 21.4 ms: 1.03x faster                                                                                                     |
| gc_traversal             | 4.49 ms                                                                                                               | 4.40 ms: 1.02x faster                                                                                                     |
| xml_etree_iterparse      | 100 ms                                                                                                                | 98.3 ms: 1.02x faster                                                                                                     |
| sqlite_synth             | 2.77 us                                                                                                               | 2.72 us: 1.02x faster                                                                                                     |
| pprint_safe_repr         | 802 ms                                                                                                                | 789 ms: 1.02x faster                                                                                                      |
| asyncio_websockets       | 397 ms                                                                                                                | 391 ms: 1.01x faster                                                                                                      |
| pprint_pformat           | 1.64 sec                                                                                                              | 1.62 sec: 1.01x faster                                                                                                    |
| pidigits                 | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| pathlib                  | 15.7 ms                                                                                                               | 15.7 ms: 1.00x slower                                                                                                     |
| python_startup_no_site   | 8.94 ms                                                                                                               | 8.97 ms: 1.00x slower                                                                                                     |
| regex_v8                 | 25.2 ms                                                                                                               | 25.3 ms: 1.00x slower                                                                                                     |
| json_loads               | 24.6 us                                                                                                               | 24.7 us: 1.01x slower                                                                                                     |
| deepcopy_reduce          | 2.86 us                                                                                                               | 2.88 us: 1.01x slower                                                                                                     |
| asyncio_tcp              | 372 ms                                                                                                                | 376 ms: 1.01x slower                                                                                                      |
| unpickle_list            | 4.69 us                                                                                                               | 4.75 us: 1.01x slower                                                                                                     |
| xml_etree_parse          | 141 ms                                                                                                                | 143 ms: 1.02x slower                                                                                                      |
| logging_silent           | 99.7 ns                                                                                                               | 102 ns: 1.02x slower                                                                                                      |
| deepcopy                 | 284 us                                                                                                                | 289 us: 1.02x slower                                                                                                      |
| typing_runtime_protocols | 176 us                                                                                                                | 179 us: 1.02x slower                                                                                                      |
| asyncio_tcp_ssl          | 1.57 sec                                                                                                              | 1.60 sec: 1.02x slower                                                                                                    |
| coverage                 | 79.6 ms                                                                                                               | 81.1 ms: 1.02x slower                                                                                                     |
| logging_format           | 6.98 us                                                                                                               | 7.13 us: 1.02x slower                                                                                                     |
| pickle_pure_python       | 321 us                                                                                                                | 328 us: 1.02x slower                                                                                                      |
| logging_simple           | 6.38 us                                                                                                               | 6.54 us: 1.02x slower                                                                                                     |
| json_dumps               | 10.6 ms                                                                                                               | 10.9 ms: 1.02x slower                                                                                                     |
| unpickle                 | 15.1 us                                                                                                               | 15.4 us: 1.02x slower                                                                                                     |
| mdp                      | 2.52 sec                                                                                                              | 2.59 sec: 1.03x slower                                                                                                    |
| scimark_monte_carlo      | 67.1 ms                                                                                                               | 69.2 ms: 1.03x slower                                                                                                     |
| meteor_contest           | 127 ms                                                                                                                | 131 ms: 1.03x slower                                                                                                      |
| regex_compile            | 142 ms                                                                                                                | 147 ms: 1.04x slower                                                                                                      |
| tornado_http             | 117 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| sympy_str                | 296 ms                                                                                                                | 309 ms: 1.04x slower                                                                                                      |
| sqlglot_parse            | 1.42 ms                                                                                                               | 1.48 ms: 1.05x slower                                                                                                     |
| pycparser                | 1.22 sec                                                                                                              | 1.28 sec: 1.05x slower                                                                                                    |
| sympy_expand             | 501 ms                                                                                                                | 524 ms: 1.05x slower                                                                                                      |
| chaos                    | 63.4 ms                                                                                                               | 66.6 ms: 1.05x slower                                                                                                     |
| thrift                   | 851 us                                                                                                                | 896 us: 1.05x slower                                                                                                      |
| pickle_list              | 4.28 us                                                                                                               | 4.51 us: 1.05x slower                                                                                                     |
| async_generators         | 359 ms                                                                                                                | 380 ms: 1.06x slower                                                                                                      |
| pickle                   | 10.2 us                                                                                                               | 10.8 us: 1.06x slower                                                                                                     |
| comprehensions           | 17.0 us                                                                                                               | 18.1 us: 1.06x slower                                                                                                     |
| pickle_dict              | 30.3 us                                                                                                               | 32.4 us: 1.07x slower                                                                                                     |
| sqlglot_transpile        | 1.80 ms                                                                                                               | 1.94 ms: 1.08x slower                                                                                                     |
| go                       | 139 ms                                                                                                                | 151 ms: 1.09x slower                                                                                                      |
| docutils                 | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| nqueens                  | 89.1 ms                                                                                                               | 97.2 ms: 1.09x slower                                                                                                     |
| django_template          | 39.5 ms                                                                                                               | 43.1 ms: 1.09x slower                                                                                                     |
| bench_thread_pool        | 857 us                                                                                                                | 939 us: 1.10x slower                                                                                                      |
| 2to3                     | 282 ms                                                                                                                | 310 ms: 1.10x slower                                                                                                      |
| raytrace                 | 286 ms                                                                                                                | 316 ms: 1.10x slower                                                                                                      |
| sympy_sum                | 152 ms                                                                                                                | 168 ms: 1.10x slower                                                                                                      |
| genshi_text              | 25.7 ms                                                                                                               | 28.3 ms: 1.10x slower                                                                                                     |
| bench_mp_pool            | 4.69 ms                                                                                                               | 5.17 ms: 1.10x slower                                                                                                     |
| genshi_xml               | 56.4 ms                                                                                                               | 62.3 ms: 1.11x slower                                                                                                     |
| sqlglot_normalize        | 116 ms                                                                                                                | 129 ms: 1.11x slower                                                                                                      |
| hexiom                   | 6.16 ms                                                                                                               | 6.95 ms: 1.13x slower                                                                                                     |
| sqlglot_optimize         | 57.9 ms                                                                                                               | 65.6 ms: 1.13x slower                                                                                                     |
| sympy_integrate          | 23.0 ms                                                                                                               | 26.3 ms: 1.14x slower                                                                                                     |
| pylint                   | 350 ms                                                                                                                | 409 ms: 1.17x slower                                                                                                      |
| generators               | 29.6 ms                                                                                                               | 36.9 ms: 1.25x slower                                                                                                     |
| unpack_sequence          | 52.6 ns                                                                                                               | 91.8 ns: 1.74x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (11): json, async_tree_none, async_tree_io, async_tree_none_tg, fannkuch, async_tree_memoization_tg, python_startup, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 79.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x