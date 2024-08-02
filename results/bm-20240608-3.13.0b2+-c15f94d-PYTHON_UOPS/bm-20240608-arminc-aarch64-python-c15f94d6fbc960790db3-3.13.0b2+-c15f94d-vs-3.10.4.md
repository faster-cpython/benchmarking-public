# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 353 ms: 1.08x faster                                                     |
| chameleon      | 10.8 ms                                                               | 10.0 ms: 1.08x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.50 sec: 1.01x faster                                                   |
| html5lib       | 86.5 ms                                                               | 72.1 ms: 1.20x faster                                                    |
| tornado_http   | 178 ms                                                                | 134 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 519 ms: 1.83x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 684 ms: 1.66x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 828 ms: 1.54x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.70x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 113 ms: 1.20x faster                                                     |
| nbody          | 166 ms                                                                | 141 ms: 1.17x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 166 ms: 1.07x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                    |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 448 us: 1.18x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 87.0 ms: 1.14x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.11 sec: 1.08x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.62 us: 1.06x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 348 us: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.37 us: 1.03x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 13.4 us: 1.07x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 16.4 ms: 1.15x faster                                                    |
| django_template | 53.3 ms                                                               | 48.9 ms: 1.09x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 36.2 ms: 1.03x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 76.1 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 222 us: 2.98x faster                                                     |
| async_tree_none          | 950 ms                                                                | 519 ms: 1.83x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 8.06 ms: 1.80x faster                                                    |
| deltablue                | 8.94 ms                                                               | 5.13 ms: 1.74x faster                                                    |
| generators               | 68.1 ms                                                               | 40.2 ms: 1.69x faster                                                    |
| raytrace                 | 573 ms                                                                | 340 ms: 1.68x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 684 ms: 1.66x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 596 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 828 ms: 1.54x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                   |
| richards_super           | 107 ms                                                                | 73.6 ms: 1.46x faster                                                    |
| chaos                    | 121 ms                                                                | 85.2 ms: 1.42x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.70 ms: 1.41x faster                                                    |
| richards                 | 91.7 ms                                                               | 66.4 ms: 1.38x faster                                                    |
| go                       | 264 ms                                                                | 196 ms: 1.35x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.32 us: 1.34x faster                                                    |
| tornado_http             | 178 ms                                                                | 134 ms: 1.33x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.02 us: 1.32x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.32x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.15 ms: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 969 us: 1.30x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                   |
| scimark_sor              | 246 ms                                                                | 199 ms: 1.24x faster                                                     |
| pylint                   | 485 ms                                                                | 393 ms: 1.23x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.4 ms: 1.22x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 72.1 ms: 1.20x faster                                                    |
| float                    | 135 ms                                                                | 113 ms: 1.20x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.18x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 448 us: 1.18x faster                                                     |
| logging_silent           | 222 ns                                                                | 188 ns: 1.18x faster                                                     |
| nbody                    | 166 ms                                                                | 141 ms: 1.17x faster                                                     |
| dask                     | 450 ms                                                                | 389 ms: 1.16x faster                                                     |
| mako                     | 18.9 ms                                                               | 16.4 ms: 1.15x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 87.0 ms: 1.14x faster                                                    |
| pyflate                  | 795 ms                                                                | 706 ms: 1.13x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.4 ms: 1.12x faster                                                    |
| comprehensions           | 33.1 us                                                               | 29.6 us: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 65.9 ms: 1.11x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 116 ms: 1.10x faster                                                     |
| django_template          | 53.3 ms                                                               | 48.9 ms: 1.09x faster                                                    |
| aiohttp                  | 1.39 ms                                                               | 1.28 ms: 1.09x faster                                                    |
| chameleon                | 10.8 ms                                                               | 10.0 ms: 1.08x faster                                                    |
| mypy2                    | 936 ms                                                                | 866 ms: 1.08x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 3.11 sec: 1.08x faster                                                   |
| 2to3                     | 381 ms                                                                | 353 ms: 1.08x faster                                                     |
| scimark_lu               | 227 ms                                                                | 211 ms: 1.07x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.35 ms: 1.07x faster                                                    |
| regex_compile            | 177 ms                                                                | 166 ms: 1.07x faster                                                     |
| sympy_sum                | 184 ms                                                                | 173 ms: 1.06x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.62 us: 1.06x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 348 us: 1.05x faster                                                     |
| sympy_str                | 329 ms                                                                | 314 ms: 1.05x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| sympy_expand             | 543 ms                                                                | 521 ms: 1.04x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 10.5 ms: 1.04x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.56 sec: 1.04x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 72.7 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.99 us: 1.03x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 26.0 ms: 1.02x faster                                                    |
| spectral_norm            | 186 ms                                                                | 183 ms: 1.02x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.50 sec: 1.01x faster                                                   |
| json                     | 5.88 ms                                                               | 5.84 ms: 1.01x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.38 sec: 1.01x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.37 us: 1.03x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 36.2 ms: 1.03x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.78 us: 1.04x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.03 ms: 1.04x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| meteor_contest           | 126 ms                                                                | 133 ms: 1.05x slower                                                     |
| deepcopy                 | 511 us                                                                | 539 us: 1.05x slower                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.05 ms: 1.06x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.41 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.07x slower                                                    |
| scimark_fft              | 500 ms                                                                | 543 ms: 1.08x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 76.1 ms: 1.09x slower                                                    |
| nqueens                  | 117 ms                                                                | 128 ms: 1.09x slower                                                     |
| unpickle                 | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 72.0 us: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| async_generators         | 452 ms                                                                | 538 ms: 1.19x slower                                                     |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 5.10 ms: 1.23x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.8 ms: 1.27x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (5): fannkuch, asyncio_websockets, pidigits, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x