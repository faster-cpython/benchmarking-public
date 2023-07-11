
# Results vs. 3.10.4

- fork: gvanrossum
- ref: new_for_iter_uops
- machine: linux-x86_64
- commit hash: 0d33f29
- commit date: 2023-07-11
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                 |
| tornado_http   | 127 ms                                                 | 96.6 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.3 ms: 1.53x faster                                                  |
| float          | 111 ms                                                 | 79.8 ms: 1.39x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.29x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.74 ms: 1.39x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.31x faster                                                  |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.15 us: 1.07x slower                                                  |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.22 ms: 1.53x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                   |
| generators               | 76.8 ms                                                | 28.7 ms: 2.67x faster                                                  |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                                  |
| asyncio_tcp              | 925 ms                                                 | 505 ms: 1.83x faster                                                   |
| chaos                    | 106 ms                                                 | 60.1 ms: 1.77x faster                                                  |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                   |
| logging_silent           | 175 ns                                                 | 104 ns: 1.69x faster                                                   |
| richards_super           | 90.7 ms                                                | 53.8 ms: 1.69x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                 |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                   |
| crypto_pyaes             | 118 ms                                                 | 71.5 ms: 1.66x faster                                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                   |
| scimark_monte_carlo      | 108 ms                                                 | 67.5 ms: 1.60x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                                  |
| richards                 | 74.9 ms                                                | 47.6 ms: 1.57x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                                   |
| python_startup           | 14.2 ms                                                | 9.22 ms: 1.53x faster                                                  |
| nbody                    | 142 ms                                                 | 92.3 ms: 1.53x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.51x faster                                                 |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                   |
| unpack_sequence          | 64.7 ns                                                | 43.3 ns: 1.50x faster                                                  |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                   |
| async_tree_none          | 717 ms                                                 | 484 ms: 1.48x faster                                                   |
| async_tree_memoization   | 854 ms                                                 | 582 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                                   |
| json_dumps               | 13.5 ms                                                | 9.74 ms: 1.39x faster                                                  |
| float                    | 111 ms                                                 | 79.8 ms: 1.39x faster                                                  |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                                  |
| coroutines               | 31.8 ms                                                | 23.1 ms: 1.37x faster                                                  |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                  |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.35x faster                                                   |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                 |
| logging_format           | 8.91 us                                                | 6.61 us: 1.35x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                                   |
| tornado_http             | 127 ms                                                 | 96.6 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 725 ms: 1.31x faster                                                   |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 57.4 ms: 1.31x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.29x faster                                                 |
| regex_compile            | 177 ms                                                 | 138 ms: 1.29x faster                                                   |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                   |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                                   |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                   |
| nqueens                  | 100 ms                                                 | 80.1 ms: 1.25x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                                  |
| fannkuch                 | 486 ms                                                 | 399 ms: 1.22x faster                                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                 |
| scimark_fft              | 424 ms                                                 | 362 ms: 1.17x faster                                                   |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                                   |
| dulwich_log              | 75.9 ms                                                | 66.6 ms: 1.14x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                  |
| json_loads               | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.96 ms: 1.10x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.09x faster                                                  |
| json                     | 5.42 ms                                                | 4.97 ms: 1.09x faster                                                  |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| mdp                      | 2.82 sec                                               | 2.67 sec: 1.06x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                                  |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                  |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                  |
| gc_traversal             | 3.84 ms                                                | 3.95 ms: 1.03x slower                                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                                   |
| unpickle_list            | 4.82 us                                                | 5.15 us: 1.07x slower                                                  |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                                  |
| telco                    | 6.54 ms                                                | 7.22 ms: 1.10x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                  |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                                  |
| dask                     | 423 ms                                                 | 522 ms: 1.24x slower                                                   |
| coverage                 | 72.8 ms                                                | 93.4 ms: 1.28x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                           |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
