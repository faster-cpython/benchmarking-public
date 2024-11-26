# Results vs. 3.10.4

- fork: python
- ref: cfbc841ef3c27b3e65d1
- machine: linux-x86_64
- commit hash: cfbc841
- commit date: 2024-09-03
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| docutils       | 3.30 sec                                               | 3.03 sec: 1.09x faster                                                |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                 |
| tornado_http   | 136 ms                                                 | 95.6 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.1 ms: 1.94x faster                                                 |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                 |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                 |
| generators               | 80.1 ms                                                | 32.9 ms: 2.43x faster                                                 |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.4 ms: 2.09x faster                                                 |
| richards                 | 79.3 ms                                                | 39.2 ms: 2.02x faster                                                 |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                 |
| nbody                    | 154 ms                                                 | 79.1 ms: 1.94x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                                  |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                 |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                  |
| go                       | 240 ms                                                 | 130 ms: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| spectral_norm            | 170 ms                                                 | 99.2 ms: 1.71x faster                                                 |
| mako                     | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                 |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                 |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.20 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                 |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.85 ms: 1.52x faster                                                 |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                  |
| tornado_http             | 136 ms                                                 | 95.6 ms: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                  |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.8 ms: 1.23x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.7 ms: 1.20x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                 |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.03 sec: 1.09x faster                                                |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| json                     | 5.69 ms                                                | 5.56 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                  |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                  |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| coverage                 | 79.4 ms                                                | 86.5 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-cfbc841-JIT/bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.431x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.22x