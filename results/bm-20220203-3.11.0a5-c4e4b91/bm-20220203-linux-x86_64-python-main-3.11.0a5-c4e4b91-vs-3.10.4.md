
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                  |
| chameleon      | 9.06 ms                                                | 6.95 ms: 1.30x faster                                 |
| html5lib       | 85.9 ms                                                | 67.9 ms: 1.26x faster                                 |
| tornado_http   | 127 ms                                                 | 106 ms: 1.21x faster                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.7 ms: 1.49x faster                                 |
| float          | 111 ms                                                 | 77.5 ms: 1.43x faster                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 140 ms: 1.26x faster                                  |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.0 ms: 1.04x faster                                 |
| regex_effbot   | 3.23 ms                                                | 3.14 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 334 us: 1.36x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 57.0 ms: 1.32x faster                                 |
| unpickle_pure_python | 300 us                                                 | 249 us: 1.21x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 79.6 ms: 1.18x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.2 ms: 1.11x faster                                 |
| json_loads           | 28.8 us                                                | 26.7 us: 1.08x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                  |
| pickle               | 10.3 us                                                | 9.93 us: 1.04x faster                                 |
| pickle_list          | 4.56 us                                                | 4.47 us: 1.02x faster                                 |
| pickle_dict          | 27.3 us                                                | 28.1 us: 1.03x slower                                 |
| unpickle_list        | 4.82 us                                                | 5.26 us: 1.09x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.13 ms: 1.74x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 5.92 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.31x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.5 ms: 1.41x faster                                 |
| django_template | 45.9 ms                                                | 35.4 ms: 1.30x faster                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 4.13 ms: 1.79x faster                                 |
| python_startup          | 14.2 ms                                                | 8.13 ms: 1.74x faster                                 |
| go                      | 229 ms                                                 | 147 ms: 1.55x faster                                  |
| logging_silent          | 175 ns                                                 | 113 ns: 1.55x faster                                  |
| scimark_sor             | 197 ms                                                 | 129 ms: 1.53x faster                                  |
| nbody                   | 142 ms                                                 | 94.7 ms: 1.49x faster                                 |
| scimark_monte_carlo     | 108 ms                                                 | 72.6 ms: 1.49x faster                                 |
| richards                | 74.9 ms                                                | 50.8 ms: 1.47x faster                                 |
| pyflate                 | 673 ms                                                 | 459 ms: 1.46x faster                                  |
| raytrace                | 464 ms                                                 | 321 ms: 1.45x faster                                  |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.44x faster                                  |
| float                   | 111 ms                                                 | 77.5 ms: 1.43x faster                                 |
| chaos                   | 106 ms                                                 | 74.9 ms: 1.42x faster                                 |
| crypto_pyaes            | 118 ms                                                 | 83.8 ms: 1.41x faster                                 |
| hexiom                  | 9.53 ms                                                | 6.76 ms: 1.41x faster                                 |
| mako                    | 14.8 ms                                                | 10.5 ms: 1.41x faster                                 |
| unpack_sequence         | 64.7 ns                                                | 46.0 ns: 1.41x faster                                 |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                 |
| logging_simple          | 8.07 us                                                | 5.84 us: 1.38x faster                                 |
| pickle_pure_python      | 455 us                                                 | 334 us: 1.36x faster                                  |
| scimark_lu              | 163 ms                                                 | 120 ms: 1.36x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 57.0 ms: 1.32x faster                                 |
| chameleon               | 9.06 ms                                                | 6.95 ms: 1.30x faster                                 |
| django_template         | 45.9 ms                                                | 35.4 ms: 1.30x faster                                 |
| thrift                  | 1.03 ms                                                | 815 us: 1.27x faster                                  |
| html5lib                | 85.9 ms                                                | 67.9 ms: 1.26x faster                                 |
| regex_compile           | 177 ms                                                 | 140 ms: 1.26x faster                                  |
| 2to3                    | 336 ms                                                 | 267 ms: 1.26x faster                                  |
| pycparser               | 1.50 sec                                               | 1.19 sec: 1.26x faster                                |
| scimark_fft             | 424 ms                                                 | 347 ms: 1.22x faster                                  |
| fannkuch                | 486 ms                                                 | 400 ms: 1.21x faster                                  |
| tornado_http            | 127 ms                                                 | 106 ms: 1.21x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 249 us: 1.21x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 79.6 ms: 1.18x faster                                 |
| dulwich_log             | 75.9 ms                                                | 65.7 ms: 1.16x faster                                 |
| nqueens                 | 100 ms                                                 | 87.2 ms: 1.15x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 21.3 ms: 1.14x faster                                 |
| json                    | 5.42 ms                                                | 4.84 ms: 1.12x faster                                 |
| json_dumps              | 13.5 ms                                                | 12.2 ms: 1.11x faster                                 |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                  |
| sympy_sum               | 185 ms                                                 | 170 ms: 1.09x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.71 us: 1.08x faster                                 |
| sympy_expand            | 545 ms                                                 | 503 ms: 1.08x faster                                  |
| sympy_str               | 328 ms                                                 | 304 ms: 1.08x faster                                  |
| json_loads              | 28.8 us                                                | 26.7 us: 1.08x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.14 ms: 1.06x faster                                 |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                  |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                  |
| regex_v8                | 25.0 ms                                                | 24.0 ms: 1.04x faster                                 |
| pickle                  | 10.3 us                                                | 9.93 us: 1.04x faster                                 |
| regex_effbot            | 3.23 ms                                                | 3.14 ms: 1.03x faster                                 |
| pickle_list             | 4.56 us                                                | 4.47 us: 1.02x faster                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.92 ms: 1.02x slower                                 |
| telco                   | 6.54 ms                                                | 6.70 ms: 1.02x slower                                 |
| pickle_dict             | 27.3 us                                                | 28.1 us: 1.03x slower                                 |
| unpickle_list           | 4.82 us                                                | 5.26 us: 1.09x slower                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x
