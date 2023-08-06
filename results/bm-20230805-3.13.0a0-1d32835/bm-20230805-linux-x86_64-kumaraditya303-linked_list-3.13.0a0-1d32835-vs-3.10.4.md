
# Results vs. 3.10.4

- fork: kumaraditya303
- ref: linked_list
- machine: linux-x86_64
- commit hash: 1d32835
- commit date: 2023-08-05
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                               |
| tornado_http   | 127 ms                                                 | 94.8 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.4 ms: 1.62x faster                                                |
| float          | 111 ms                                                 | 79.4 ms: 1.39x faster                                                |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                 |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                 |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                                 |
| json_dumps           | 13.5 ms                                                | 9.70 ms: 1.40x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                |
| tomli_loads          | 2.92 sec                                               | 2.32 sec: 1.26x faster                                               |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 83.9 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                                |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                                |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.47x faster                                                 |
| generators               | 76.8 ms                                                | 28.2 ms: 2.72x faster                                                |
| deltablue                | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                |
| asyncio_tcp              | 925 ms                                                 | 483 ms: 1.91x faster                                                 |
| chaos                    | 106 ms                                                 | 59.2 ms: 1.79x faster                                                |
| async_tree_none          | 717 ms                                                 | 405 ms: 1.77x faster                                                 |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 68.6 ms: 1.73x faster                                                |
| richards_super           | 90.7 ms                                                | 52.6 ms: 1.72x faster                                                |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                                 |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                               |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 66.8 ms: 1.62x faster                                                |
| richards                 | 74.9 ms                                                | 46.3 ms: 1.62x faster                                                |
| nbody                    | 142 ms                                                 | 87.4 ms: 1.62x faster                                                |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                |
| hexiom                   | 9.53 ms                                                | 5.95 ms: 1.60x faster                                                |
| async_tree_memoization   | 854 ms                                                 | 540 ms: 1.58x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.14 sec: 1.55x faster                                               |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                |
| python_startup           | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                |
| pyflate                  | 673 ms                                                 | 447 ms: 1.51x faster                                                 |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 643 ms: 1.48x faster                                                 |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.70 ms: 1.40x faster                                                |
| float                    | 111 ms                                                 | 79.4 ms: 1.39x faster                                                |
| logging_format           | 8.91 us                                                | 6.41 us: 1.39x faster                                                |
| logging_simple           | 8.07 us                                                | 5.84 us: 1.38x faster                                                |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                                |
| pprint_pformat           | 1.99 sec                                               | 1.45 sec: 1.37x faster                                               |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 709 ms: 1.35x faster                                                 |
| tornado_http             | 127 ms                                                 | 94.8 ms: 1.34x faster                                                |
| unpack_sequence          | 64.7 ns                                                | 48.5 ns: 1.34x faster                                                |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                                |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                               |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                                 |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.32 sec: 1.26x faster                                               |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                                |
| deepcopy                 | 442 us                                                 | 352 us: 1.25x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.3 ms: 1.25x faster                                                |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                |
| scimark_fft              | 424 ms                                                 | 350 ms: 1.21x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                               |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.71 ms: 1.16x faster                                                |
| bench_thread_pool        | 947 us                                                 | 821 us: 1.15x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                                |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                                |
| xml_etree_generate       | 94.2 ms                                                | 83.9 ms: 1.12x faster                                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                 |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.68 sec: 1.05x faster                                               |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                 |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                                |
| unpickle                 | 14.1 us                                                | 14.6 us: 1.03x slower                                                |
| gc_traversal             | 3.84 ms                                                | 3.98 ms: 1.04x slower                                                |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.47 ms: 1.07x slower                                                |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                                |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                |
| telco                    | 6.54 ms                                                | 7.83 ms: 1.20x slower                                                |
| dask                     | 423 ms                                                 | 515 ms: 1.22x slower                                                 |
| coverage                 | 72.8 ms                                                | 93.1 ms: 1.28x slower                                                |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
