
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 256 ms: 1.31x faster                                  |
| chameleon      | 9.06 ms                                                | 6.57 ms: 1.38x faster                                 |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                 |
| tornado_http   | 127 ms                                                 | 94.6 ms: 1.35x faster                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                 |
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                 |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                 |
| regex_effbot   | 3.23 ms                                                | 2.93 ms: 1.10x faster                                 |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                 |
| unpickle_pure_python | 300 us                                                 | 229 us: 1.31x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.5 ms: 1.23x faster                                 |
| json_loads           | 28.8 us                                                | 25.4 us: 1.14x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.4 ms: 1.10x faster                                 |
| pickle               | 10.3 us                                                | 9.56 us: 1.08x faster                                 |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| pickle_dict          | 27.3 us                                                | 25.6 us: 1.06x faster                                 |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.25 ms: 1.71x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.16 ms: 1.06x slower                                 |
| Geometric mean         | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.88 ms: 1.49x faster                                 |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.61 ms: 2.06x faster                                 |
| logging_silent          | 175 ns                                                 | 98.2 ns: 1.78x faster                                 |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.72x faster                                  |
| python_startup          | 14.2 ms                                                | 8.25 ms: 1.71x faster                                 |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                  |
| pyflate                 | 673 ms                                                 | 411 ms: 1.64x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 66.5 ms: 1.63x faster                                 |
| richards                | 74.9 ms                                                | 46.4 ms: 1.61x faster                                 |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.60x faster                                 |
| raytrace                | 464 ms                                                 | 294 ms: 1.58x faster                                  |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                 |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.54x faster                                 |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                 |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                 |
| hexiom                  | 9.53 ms                                                | 6.29 ms: 1.52x faster                                 |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.88 ms: 1.49x faster                                 |
| pickle_pure_python      | 455 us                                                 | 305 us: 1.49x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 44.3 ns: 1.46x faster                                 |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                 |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                 |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                  |
| logging_format          | 8.91 us                                                | 6.44 us: 1.38x faster                                 |
| chameleon               | 9.06 ms                                                | 6.57 ms: 1.38x faster                                 |
| logging_simple          | 8.07 us                                                | 5.89 us: 1.37x faster                                 |
| tornado_http            | 127 ms                                                 | 94.6 ms: 1.35x faster                                 |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 229 us: 1.31x faster                                  |
| 2to3                    | 336 ms                                                 | 256 ms: 1.31x faster                                  |
| scimark_fft             | 424 ms                                                 | 325 ms: 1.30x faster                                  |
| pycparser               | 1.50 sec                                               | 1.18 sec: 1.27x faster                                |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.5 ms: 1.23x faster                                 |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.57 ms: 1.19x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                 |
| nqueens                 | 100 ms                                                 | 84.7 ms: 1.18x faster                                 |
| sympy_expand            | 545 ms                                                 | 468 ms: 1.17x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.53 us: 1.16x faster                                 |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                 |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                  |
| sympy_sum               | 185 ms                                                 | 161 ms: 1.15x faster                                  |
| json_loads              | 28.8 us                                                | 25.4 us: 1.14x faster                                 |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                 |
| json                    | 5.42 ms                                                | 4.91 ms: 1.10x faster                                 |
| regex_effbot            | 3.23 ms                                                | 2.93 ms: 1.10x faster                                 |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.4 ms: 1.10x faster                                 |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                  |
| pickle                  | 10.3 us                                                | 9.56 us: 1.08x faster                                 |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| pickle_dict             | 27.3 us                                                | 25.6 us: 1.06x faster                                 |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| telco                   | 6.54 ms                                                | 6.84 ms: 1.05x slower                                 |
| unpickle_list           | 4.82 us                                                | 5.05 us: 1.05x slower                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.16 ms: 1.06x slower                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                          |
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x
