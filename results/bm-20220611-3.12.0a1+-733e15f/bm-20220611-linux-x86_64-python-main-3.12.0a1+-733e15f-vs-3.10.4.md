
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 733e15f
- commit date: 2022-06-11
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.40 ms: 1.41x faster                                  |
| html5lib       | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| tornado_http   | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.0 ms: 1.56x faster                                  |
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 198 ms: 1.12x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.01 ms: 1.07x faster                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.56x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.1 ms: 1.44x faster                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.41x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 75.4 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.0 ms: 1.13x faster                                  |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.89 us: 1.01x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.26 ms: 1.71x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.11 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.74 ms: 1.52x faster                                  |
| django_template | 45.9 ms                                                | 31.2 ms: 1.47x faster                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.51 ms: 2.11x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.78x faster                                   |
| logging_silent          | 175 ns                                                 | 99.2 ns: 1.76x faster                                  |
| go                      | 229 ms                                                 | 131 ms: 1.74x faster                                   |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                  |
| python_startup          | 14.2 ms                                                | 8.26 ms: 1.71x faster                                  |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                   |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                  |
| scimark_lu              | 163 ms                                                 | 102 ms: 1.60x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.0 ms: 1.60x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.3 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.56x faster                                  |
| float                   | 111 ms                                                 | 71.0 ms: 1.56x faster                                  |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.56x faster                                   |
| nbody                   | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.17 ms: 1.54x faster                                  |
| mako                    | 14.8 ms                                                | 9.74 ms: 1.52x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.6 ns: 1.49x faster                                  |
| django_template         | 45.9 ms                                                | 31.2 ms: 1.47x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 52.1 ms: 1.44x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 212 us: 1.41x faster                                   |
| chameleon               | 9.06 ms                                                | 6.40 ms: 1.41x faster                                  |
| pycparser               | 1.50 sec                                               | 1.07 sec: 1.41x faster                                 |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                  |
| tornado_http            | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                   |
| logging_simple          | 8.07 us                                                | 5.84 us: 1.38x faster                                  |
| html5lib                | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.35x faster                                   |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| fannkuch                | 486 ms                                                 | 382 ms: 1.27x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.36 ms: 1.25x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.4 ms: 1.25x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.9 ms: 1.23x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                  |
| nqueens                 | 100 ms                                                 | 83.4 ms: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.50 us: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| json_loads              | 28.8 us                                                | 25.1 us: 1.15x faster                                  |
| json                    | 5.42 ms                                                | 4.78 ms: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| json_dumps              | 13.5 ms                                                | 12.0 ms: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| regex_dna               | 222 ms                                                 | 198 ms: 1.12x faster                                   |
| pickle_list             | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| regex_effbot            | 3.23 ms                                                | 3.01 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.02x faster                                   |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.89 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.11 ms: 1.05x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (2): pickle, unpickle
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x
