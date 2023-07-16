
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 266 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| tornado_http   | 127 ms                                                 | 98.6 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.5 ms: 1.58x faster                                  |
| float          | 111 ms                                                 | 79.8 ms: 1.38x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.72 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.46x faster                                   |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.87 ms: 1.37x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.9 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.7 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| pickle_list          | 4.56 us                                                | 4.70 us: 1.03x slower                                  |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.26 ms: 1.53x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.73 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                   |
| generators               | 76.8 ms                                                | 30.4 ms: 2.52x faster                                  |
| deltablue                | 7.42 ms                                                | 3.51 ms: 2.11x faster                                  |
| richards_super           | 90.7 ms                                                | 49.9 ms: 1.82x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.82x faster                                   |
| logging_silent           | 175 ns                                                 | 97.9 ns: 1.79x faster                                  |
| richards                 | 74.9 ms                                                | 44.1 ms: 1.70x faster                                  |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                   |
| chaos                    | 106 ms                                                 | 63.4 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                 |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.62x faster                                   |
| nbody                    | 142 ms                                                 | 89.5 ms: 1.58x faster                                  |
| raytrace                 | 464 ms                                                 | 298 ms: 1.55x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 76.7 ms: 1.54x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.15 sec: 1.54x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.19 ms: 1.54x faster                                  |
| async_tree_none          | 717 ms                                                 | 467 ms: 1.53x faster                                   |
| python_startup           | 14.2 ms                                                | 9.26 ms: 1.53x faster                                  |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 569 ms: 1.50x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                  |
| pickle_pure_python       | 455 us                                                 | 311 us: 1.46x faster                                   |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.46x faster                                   |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                   |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                  |
| float                    | 111 ms                                                 | 79.8 ms: 1.38x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.87 ms: 1.37x faster                                  |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                  |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 707 ms: 1.35x faster                                   |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 721 ms: 1.33x faster                                   |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.29x faster                                 |
| tornado_http             | 127 ms                                                 | 98.6 ms: 1.29x faster                                  |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                  |
| logging_simple           | 8.07 us                                                | 6.29 us: 1.28x faster                                  |
| logging_format           | 8.91 us                                                | 7.00 us: 1.27x faster                                  |
| 2to3                     | 336 ms                                                 | 266 ms: 1.26x faster                                   |
| xml_etree_process        | 74.9 ms                                                | 59.9 ms: 1.25x faster                                  |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| nqueens                  | 100 ms                                                 | 80.9 ms: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 393 ms: 1.24x faster                                   |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                   |
| regex_compile            | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.8 ms: 1.21x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 53.9 ns: 1.20x faster                                  |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                   |
| docutils                 | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.3 ms: 1.16x faster                                  |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                   |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                   |
| dulwich_log              | 75.9 ms                                                | 67.7 ms: 1.12x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                  |
| json_loads               | 28.8 us                                                | 25.9 us: 1.11x faster                                  |
| regex_v8                 | 25.0 ms                                                | 22.6 ms: 1.11x faster                                  |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.95 ms: 1.10x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 85.7 ms: 1.10x faster                                  |
| mdp                      | 2.82 sec                                               | 2.59 sec: 1.09x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| json                     | 5.42 ms                                                | 5.04 ms: 1.07x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                   |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                  |
| unpickle_list            | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| pickle_list              | 4.56 us                                                | 4.70 us: 1.03x slower                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| async_generators         | 425 ms                                                 | 442 ms: 1.04x slower                                   |
| telco                    | 6.54 ms                                                | 6.88 ms: 1.05x slower                                  |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                  |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.72 ms: 1.15x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.73 ms: 1.16x slower                                  |
| dask                     | 423 ms                                                 | 534 ms: 1.26x slower                                   |
| coverage                 | 72.8 ms                                                | 94.2 ms: 1.29x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
