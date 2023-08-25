
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 264 ms: 1.27x faster                                  |
| chameleon      | 9.06 ms                                                | 7.55 ms: 1.20x faster                                 |
| html5lib       | 85.9 ms                                                | 68.1 ms: 1.26x faster                                 |
| tornado_http   | 127 ms                                                 | 107 ms: 1.19x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.1 ms: 1.49x faster                                 |
| float          | 111 ms                                                 | 78.0 ms: 1.42x faster                                 |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.8 ms: 1.01x faster                                 |
| regex_effbot   | 3.23 ms                                                | 3.25 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 329 us: 1.38x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 56.9 ms: 1.32x faster                                 |
| unpickle_pure_python | 300 us                                                 | 254 us: 1.18x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.2 ms: 1.17x faster                                 |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.4 ms: 1.10x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.06x faster                                  |
| pickle_list          | 4.56 us                                                | 4.37 us: 1.04x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                  |
| pickle               | 10.3 us                                                | 9.95 us: 1.03x faster                                 |
| pickle_dict          | 27.3 us                                                | 26.8 us: 1.02x faster                                 |
| unpickle             | 14.1 us                                                | 14.3 us: 1.01x slower                                 |
| unpickle_list        | 4.82 us                                                | 5.20 us: 1.08x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 5.85 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.32x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 45.9 ms                                                | 35.2 ms: 1.30x faster                                 |
| mako            | 14.8 ms                                                | 11.5 ms: 1.28x faster                                 |
| Geometric mean  | (ref)                                                  | 1.29x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 4.16 ms: 1.78x faster                                 |
| python_startup          | 14.2 ms                                                | 8.07 ms: 1.75x faster                                 |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.58x faster                                  |
| go                      | 229 ms                                                 | 148 ms: 1.55x faster                                  |
| logging_silent          | 175 ns                                                 | 113 ns: 1.54x faster                                  |
| pyflate                 | 673 ms                                                 | 444 ms: 1.52x faster                                  |
| spectral_norm           | 150 ms                                                 | 99.0 ms: 1.51x faster                                 |
| scimark_monte_carlo     | 108 ms                                                 | 72.7 ms: 1.49x faster                                 |
| nbody                   | 142 ms                                                 | 95.1 ms: 1.49x faster                                 |
| chaos                   | 106 ms                                                 | 72.7 ms: 1.46x faster                                 |
| richards                | 74.9 ms                                                | 51.5 ms: 1.45x faster                                 |
| raytrace                | 464 ms                                                 | 320 ms: 1.45x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 44.8 ns: 1.45x faster                                 |
| hexiom                  | 9.53 ms                                                | 6.63 ms: 1.44x faster                                 |
| scimark_lu              | 163 ms                                                 | 114 ms: 1.43x faster                                  |
| float                   | 111 ms                                                 | 78.0 ms: 1.42x faster                                 |
| crypto_pyaes            | 118 ms                                                 | 83.8 ms: 1.41x faster                                 |
| pickle_pure_python      | 455 us                                                 | 329 us: 1.38x faster                                  |
| logging_format          | 8.91 us                                                | 6.51 us: 1.37x faster                                 |
| logging_simple          | 8.07 us                                                | 5.95 us: 1.36x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 56.9 ms: 1.32x faster                                 |
| django_template         | 45.9 ms                                                | 35.2 ms: 1.30x faster                                 |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.29x faster                                |
| scimark_fft             | 424 ms                                                 | 330 ms: 1.29x faster                                  |
| mako                    | 14.8 ms                                                | 11.5 ms: 1.28x faster                                 |
| regex_compile           | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| 2to3                    | 336 ms                                                 | 264 ms: 1.27x faster                                  |
| thrift                  | 1.03 ms                                                | 812 us: 1.27x faster                                  |
| html5lib                | 85.9 ms                                                | 68.1 ms: 1.26x faster                                 |
| fannkuch                | 486 ms                                                 | 392 ms: 1.24x faster                                  |
| chameleon               | 9.06 ms                                                | 7.55 ms: 1.20x faster                                 |
| tornado_http            | 127 ms                                                 | 107 ms: 1.19x faster                                  |
| nqueens                 | 100 ms                                                 | 84.0 ms: 1.19x faster                                 |
| unpickle_pure_python    | 300 us                                                 | 254 us: 1.18x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.2 ms: 1.17x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.69 ms: 1.16x faster                                 |
| dulwich_log             | 75.9 ms                                                | 65.8 ms: 1.15x faster                                 |
| json_loads              | 28.8 us                                                | 25.1 us: 1.15x faster                                 |
| json                    | 5.42 ms                                                | 4.74 ms: 1.14x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 21.4 ms: 1.14x faster                                 |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.4 ms: 1.10x faster                                 |
| sympy_str               | 328 ms                                                 | 302 ms: 1.09x faster                                  |
| sympy_sum               | 185 ms                                                 | 170 ms: 1.09x faster                                  |
| sympy_expand            | 545 ms                                                 | 506 ms: 1.08x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.73 us: 1.07x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.06x faster                                  |
| pathlib                 | 20.0 ms                                                | 19.1 ms: 1.05x faster                                 |
| regex_dna               | 222 ms                                                 | 212 ms: 1.05x faster                                  |
| pickle_list             | 4.56 us                                                | 4.37 us: 1.04x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                  |
| pickle                  | 10.3 us                                                | 9.95 us: 1.03x faster                                 |
| pickle_dict             | 27.3 us                                                | 26.8 us: 1.02x faster                                 |
| regex_v8                | 25.0 ms                                                | 24.8 ms: 1.01x faster                                 |
| regex_effbot            | 3.23 ms                                                | 3.25 ms: 1.01x slower                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.85 ms: 1.01x slower                                 |
| unpickle                | 14.1 us                                                | 14.3 us: 1.01x slower                                 |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| telco                   | 6.54 ms                                                | 6.69 ms: 1.02x slower                                 |
| unpickle_list           | 4.82 us                                                | 5.20 us: 1.08x slower                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                          |
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
