
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 38612a0
- commit date: 2022-06-26
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.45 ms: 1.40x faster                                  |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.38x faster                                  |
| tornado_http   | 127 ms                                                 | 92.1 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.1 ms: 1.55x faster                                  |
| nbody          | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.0 ms: 1.44x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 24.5 us: 1.18x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.0 ms: 1.12x faster                                  |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.1 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.26 ms: 1.71x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.10 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.46 ms: 1.56x faster                                  |
| django_template | 45.9 ms                                                | 31.6 ms: 1.45x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                  |
| logging_silent          | 175 ns                                                 | 89.6 ns: 1.95x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                   |
| go                      | 229 ms                                                 | 128 ms: 1.79x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 62.4 ms: 1.73x faster                                  |
| python_startup          | 14.2 ms                                                | 8.26 ms: 1.71x faster                                  |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                   |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                   |
| chaos                   | 106 ms                                                 | 63.8 ms: 1.66x faster                                  |
| richards                | 74.9 ms                                                | 45.4 ms: 1.65x faster                                  |
| spectral_norm           | 150 ms                                                 | 92.8 ms: 1.62x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                  |
| scimark_lu              | 163 ms                                                 | 104 ms: 1.57x faster                                   |
| mako                    | 14.8 ms                                                | 9.46 ms: 1.56x faster                                  |
| float                   | 111 ms                                                 | 71.1 ms: 1.55x faster                                  |
| pickle_pure_python      | 455 us                                                 | 294 us: 1.55x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| django_template         | 45.9 ms                                                | 31.6 ms: 1.45x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 52.0 ms: 1.44x faster                                  |
| pycparser               | 1.50 sec                                               | 1.05 sec: 1.43x faster                                 |
| chameleon               | 9.06 ms                                                | 6.45 ms: 1.40x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.89 ms: 1.40x faster                                  |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                  |
| logging_format          | 8.91 us                                                | 6.40 us: 1.39x faster                                  |
| scimark_fft             | 424 ms                                                 | 304 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                   |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.38x faster                                  |
| tornado_http            | 127 ms                                                 | 92.1 ms: 1.38x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.7 ms: 1.23x faster                                  |
| nqueens                 | 100 ms                                                 | 82.2 ms: 1.22x faster                                  |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                  |
| sympy_str               | 328 ms                                                 | 277 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| json_loads              | 28.8 us                                                | 24.5 us: 1.18x faster                                  |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.72 ms: 1.15x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.0 ms: 1.12x faster                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                  |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.10 ms: 1.05x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.1 us: 1.11x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.61 ms: 1.12x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.23x
