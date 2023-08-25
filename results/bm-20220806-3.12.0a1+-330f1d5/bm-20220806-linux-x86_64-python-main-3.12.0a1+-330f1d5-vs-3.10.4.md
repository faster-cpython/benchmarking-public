
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 330f1d5
- commit date: 2022-08-06
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.50 ms: 1.39x faster                                  |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| tornado_http   | 127 ms                                                 | 91.7 ms: 1.39x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.8 ms: 1.21x faster                                  |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.2 ms: 1.44x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 24.6 us: 1.17x faster                                  |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.15 ms: 1.74x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.50 ms: 1.55x faster                                  |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| Geometric mean  | (ref)                                                  | 1.48x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                  |
| logging_silent          | 175 ns                                                 | 89.9 ns: 1.95x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                   |
| go                      | 229 ms                                                 | 131 ms: 1.75x faster                                   |
| python_startup          | 14.2 ms                                                | 8.15 ms: 1.74x faster                                  |
| pyflate                 | 673 ms                                                 | 393 ms: 1.71x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.2 ms: 1.69x faster                                  |
| richards                | 74.9 ms                                                | 44.5 ms: 1.68x faster                                  |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                   |
| mako                    | 14.8 ms                                                | 9.50 ms: 1.55x faster                                  |
| nbody                   | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                   |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                  |
| pycparser               | 1.50 sec                                               | 1.04 sec: 1.44x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 52.2 ms: 1.44x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 45.9 ns: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.91 ms: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| chameleon               | 9.06 ms                                                | 6.50 ms: 1.39x faster                                  |
| tornado_http            | 127 ms                                                 | 91.7 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                   |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                   |
| 2to3                    | 336 ms                                                 | 248 ms: 1.35x faster                                   |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                   |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.2 ms: 1.24x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.8 ms: 1.21x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                   |
| json_loads              | 28.8 us                                                | 24.6 us: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                   |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                  |
| sympy_sum               | 185 ms                                                 | 160 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.13x faster                                   |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                  |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.06 us: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
