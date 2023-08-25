
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 32ac98e
- commit date: 2022-08-13
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.30 ms: 1.44x faster                                  |
| html5lib       | 85.9 ms                                                | 62.9 ms: 1.37x faster                                  |
| tornado_http   | 127 ms                                                 | 91.6 ms: 1.39x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 51.3 ms: 1.46x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.67 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 74.3 ms: 1.27x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.17 ms: 1.73x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.04 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.21 ms: 1.60x faster                                  |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| Geometric mean  | (ref)                                                  | 1.50x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                  |
| logging_silent          | 175 ns                                                 | 89.6 ns: 1.95x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                   |
| python_startup          | 14.2 ms                                                | 8.17 ms: 1.73x faster                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                   |
| pyflate                 | 673 ms                                                 | 397 ms: 1.70x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.7 ms: 1.67x faster                                  |
| richards                | 74.9 ms                                                | 45.1 ms: 1.66x faster                                  |
| mako                    | 14.8 ms                                                | 9.21 ms: 1.60x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.97 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                   |
| raytrace                | 464 ms                                                 | 293 ms: 1.58x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.58x faster                                  |
| nbody                   | 142 ms                                                 | 91.3 ms: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                   |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.0 ns: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 51.3 ms: 1.46x faster                                  |
| chameleon               | 9.06 ms                                                | 6.30 ms: 1.44x faster                                  |
| pycparser               | 1.50 sec                                               | 1.05 sec: 1.43x faster                                 |
| thrift                  | 1.03 ms                                                | 728 us: 1.42x faster                                   |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.67 ms: 1.40x faster                                  |
| logging_format          | 8.91 us                                                | 6.39 us: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| tornado_http            | 127 ms                                                 | 91.6 ms: 1.39x faster                                  |
| logging_simple          | 8.07 us                                                | 5.81 us: 1.39x faster                                  |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                   |
| html5lib                | 85.9 ms                                                | 62.9 ms: 1.37x faster                                  |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| fannkuch                | 486 ms                                                 | 375 ms: 1.30x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 74.3 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.6 ms: 1.23x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 278 ms: 1.18x faster                                   |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                  |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                  |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.07x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| telco                   | 6.54 ms                                                | 6.47 ms: 1.01x faster                                  |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.04 ms: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.42 ms: 1.06x slower                                  |
| pidigits                | 190 ms                                                 | 201 ms: 1.06x slower                                   |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.24x
