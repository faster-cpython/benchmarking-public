
# Results vs. 3.11.0

- fork: brandtbucher
- ref: always_inline
- machine: linux-x86_64
- commit hash: 2cb76fa
- commit date: 2023-05-11
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                                  |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                |
| tornado_http   | 96.3 ms                                                | 99.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                 |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| float          | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                 |
| regex_v8       | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                 |
| regex_dna      | 204 ms                                                 | 203 ms: 1.01x faster                                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                 |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                |
| unpickle_list        | 4.91 us                                                | 4.86 us: 1.01x faster                                                 |
| pickle_pure_python   | 306 us                                                 | 314 us: 1.03x slower                                                  |
| pickle_dict          | 31.1 us                                                | 32.8 us: 1.05x slower                                                 |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.20 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.28x faster                                                  |
| generators               | 73.5 ms                                                | 31.2 ms: 2.36x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                 |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                                  |
| regex_effbot             | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                 |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                                |
| coroutines               | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                 |
| richards_super           | 56.8 ms                                                | 51.1 ms: 1.11x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 573 ms: 1.09x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.08x faster                                                 |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                                 |
| chaos                    | 69.2 ms                                                | 65.6 ms: 1.05x faster                                                 |
| regex_v8                 | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.83 ms: 1.05x faster                                                 |
| nbody                    | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                 |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 219 us: 1.04x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 711 ms: 1.04x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.35 ms: 1.04x faster                                                 |
| coverage                 | 100 ms                                                 | 96.5 ms: 1.04x faster                                                 |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.21 ms: 1.03x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.58 ms: 1.03x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                 |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| richards                 | 45.7 ms                                                | 44.9 ms: 1.02x faster                                                 |
| nqueens                  | 83.4 ms                                                | 82.0 ms: 1.02x faster                                                 |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                |
| unpickle_list            | 4.91 us                                                | 4.86 us: 1.01x faster                                                 |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                                  |
| regex_dna                | 204 ms                                                 | 203 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                 |
| bench_thread_pool        | 819 us                                                 | 827 us: 1.01x slower                                                  |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.9 ms: 1.02x slower                                                 |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                                 |
| raytrace                 | 297 ms                                                 | 302 ms: 1.02x slower                                                  |
| pickle_pure_python       | 306 us                                                 | 314 us: 1.03x slower                                                  |
| telco                    | 6.58 ms                                                | 6.78 ms: 1.03x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                |
| tornado_http             | 96.3 ms                                                | 99.6 ms: 1.03x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.5 ms: 1.04x slower                                                 |
| 2to3                     | 259 ms                                                 | 269 ms: 1.04x slower                                                  |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                  |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                                  |
| crypto_pyaes             | 74.7 ms                                                | 78.1 ms: 1.05x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 38.8 us: 1.05x slower                                                 |
| deepcopy                 | 342 us                                                 | 358 us: 1.05x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| logging_simple           | 6.03 us                                                | 6.34 us: 1.05x slower                                                 |
| pickle_dict              | 31.1 us                                                | 32.8 us: 1.05x slower                                                 |
| logging_format           | 6.68 us                                                | 7.04 us: 1.05x slower                                                 |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                  |
| float                    | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 68.0 ms: 1.07x slower                                                 |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.6 us: 1.07x slower                                                 |
| scimark_lu               | 110 ms                                                 | 118 ms: 1.07x slower                                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.82 ms: 1.07x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.20 ms: 1.08x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 74.0 ms: 1.09x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                 |
| scimark_fft              | 328 ms                                                 | 359 ms: 1.09x slower                                                  |
| unpack_sequence          | 43.1 ns                                                | 47.1 ns: 1.09x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.64 us: 1.13x slower                                                 |
| async_generators         | 368 ms                                                 | 459 ms: 1.25x slower                                                  |
| dask                     | 360 ms                                                 | 538 ms: 1.49x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
