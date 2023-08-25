
# Results vs. 3.10.4

- fork: python
- ref: 1858db7cbdbf41aa600c
- machine: linux-x86_64
- commit hash: 1858db7
- commit date: 2023-06-19
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| tornado_http   | 127 ms                                                 | 97.5 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                                 |
| float          | 111 ms                                                 | 79.5 ms: 1.39x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                 |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 308 us: 1.48x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                 |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.5 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                 |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                 |
| pickle_list          | 4.56 us                                                | 4.69 us: 1.03x slower                                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.63x faster                                                  |
| generators               | 76.8 ms                                                | 29.6 ms: 2.60x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.28 ms: 2.26x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.82x faster                                                  |
| richards_super           | 90.7 ms                                                | 50.3 ms: 1.80x faster                                                 |
| logging_silent           | 175 ns                                                 | 101 ns: 1.74x faster                                                  |
| chaos                    | 106 ms                                                 | 61.8 ms: 1.72x faster                                                 |
| richards                 | 74.9 ms                                                | 44.2 ms: 1.70x faster                                                 |
| go                       | 229 ms                                                 | 135 ms: 1.69x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                  |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                                  |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 76.7 ms: 1.54x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.2 ms: 1.52x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.63 ms: 1.50x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 43.3 ns: 1.49x faster                                                 |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                |
| async_tree_none          | 717 ms                                                 | 484 ms: 1.48x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 308 us: 1.48x faster                                                  |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 588 ms: 1.45x faster                                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| float                    | 111 ms                                                 | 79.5 ms: 1.39x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                 |
| logging_format           | 8.91 us                                                | 6.57 us: 1.36x faster                                                 |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                |
| logging_simple           | 8.07 us                                                | 6.09 us: 1.33x faster                                                 |
| pycparser                | 1.50 sec                                               | 1.13 sec: 1.32x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 726 ms: 1.31x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 729 ms: 1.31x faster                                                  |
| tornado_http             | 127 ms                                                 | 97.5 ms: 1.31x faster                                                 |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                 |
| mypy2                    | 428 ms                                                 | 339 ms: 1.27x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.2 ms: 1.26x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                                  |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                                  |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                  |
| scimark_fft              | 424 ms                                                 | 344 ms: 1.23x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.63 ms: 1.18x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 65.4 ms: 1.16x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 821 us: 1.15x faster                                                  |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                 |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.12x faster                                                |
| xml_etree_generate       | 94.2 ms                                                | 84.5 ms: 1.11x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                 |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.71 us: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                 |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| gc_traversal             | 3.84 ms                                                | 3.93 ms: 1.02x slower                                                 |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.95 us: 1.03x slower                                                 |
| pickle_list              | 4.56 us                                                | 4.69 us: 1.03x slower                                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| telco                    | 6.54 ms                                                | 6.91 ms: 1.06x slower                                                 |
| async_generators         | 425 ms                                                 | 458 ms: 1.08x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.50 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                                  |
| coverage                 | 72.8 ms                                                | 93.4 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
