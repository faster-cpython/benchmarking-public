
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.26x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| chameleon      | 9.13 ms                                                             | 6.87 ms: 1.33x faster                                 |
| html5lib       | 86.4 ms                                                             | 65.3 ms: 1.32x faster                                 |
| tornado_http   | 129 ms                                                              | 95.4 ms: 1.35x faster                                 |
| Geometric mean | (ref)                                                               | 1.32x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 146 ms                                                              | 95.2 ms: 1.53x faster                                 |
| float          | 110 ms                                                              | 74.4 ms: 1.48x faster                                 |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                               | 1.30x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 137 ms: 1.29x faster                                  |
| regex_effbot   | 3.22 ms                                                             | 3.34 ms: 1.04x slower                                 |
| regex_v8       | 24.9 ms                                                             | 25.9 ms: 1.04x slower                                 |
| regex_dna      | 213 ms                                                              | 231 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 311 us: 1.47x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 55.2 ms: 1.35x faster                                 |
| unpickle_pure_python | 300 us                                                              | 231 us: 1.30x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 78.5 ms: 1.21x faster                                 |
| json_dumps           | 13.7 ms                                                             | 12.5 ms: 1.10x faster                                 |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| pickle               | 10.2 us                                                             | 9.55 us: 1.07x faster                                 |
| unpickle             | 15.0 us                                                             | 14.1 us: 1.06x faster                                 |
| xml_etree_parse      | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| json_loads           | 29.3 us                                                             | 28.1 us: 1.04x faster                                 |
| pickle_list          | 4.73 us                                                             | 4.57 us: 1.04x faster                                 |
| pickle_dict          | 27.8 us                                                             | 27.6 us: 1.00x faster                                 |
| unpickle_list        | 4.94 us                                                             | 4.97 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                               | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.80 ms                                                             | 5.98 ms: 1.03x slower                                 |
| Geometric mean         | (ref)                                                               | 1.30x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.2 ms: 1.45x faster                                 |
| django_template | 45.8 ms                                                             | 34.3 ms: 1.34x faster                                 |
| Geometric mean  | (ref)                                                               | 1.39x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.70 ms: 1.97x faster                                 |
| python_startup          | 14.1 ms                                                             | 8.07 ms: 1.75x faster                                 |
| logging_silent          | 169 ns                                                              | 104 ns: 1.63x faster                                  |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.61x faster                                  |
| go                      | 226 ms                                                              | 143 ms: 1.58x faster                                  |
| richards                | 74.2 ms                                                             | 47.5 ms: 1.56x faster                                 |
| raytrace                | 470 ms                                                              | 306 ms: 1.54x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 70.8 ms: 1.53x faster                                 |
| nbody                   | 146 ms                                                              | 95.2 ms: 1.53x faster                                 |
| pyflate                 | 671 ms                                                              | 438 ms: 1.53x faster                                  |
| chaos                   | 106 ms                                                              | 70.2 ms: 1.51x faster                                 |
| scimark_lu              | 160 ms                                                              | 108 ms: 1.48x faster                                  |
| float                   | 110 ms                                                              | 74.4 ms: 1.48x faster                                 |
| pickle_pure_python      | 457 us                                                              | 311 us: 1.47x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 44.9 ns: 1.46x faster                                 |
| mako                    | 14.7 ms                                                             | 10.2 ms: 1.45x faster                                 |
| spectral_norm           | 150 ms                                                              | 105 ms: 1.44x faster                                  |
| logging_format          | 9.07 us                                                             | 6.35 us: 1.43x faster                                 |
| logging_simple          | 8.21 us                                                             | 5.80 us: 1.41x faster                                 |
| crypto_pyaes            | 117 ms                                                              | 82.7 ms: 1.41x faster                                 |
| hexiom                  | 9.50 ms                                                             | 6.84 ms: 1.39x faster                                 |
| thrift                  | 1.04 ms                                                             | 762 us: 1.36x faster                                  |
| xml_etree_process       | 74.8 ms                                                             | 55.2 ms: 1.35x faster                                 |
| tornado_http            | 129 ms                                                              | 95.4 ms: 1.35x faster                                 |
| django_template         | 45.8 ms                                                             | 34.3 ms: 1.34x faster                                 |
| chameleon               | 9.13 ms                                                             | 6.87 ms: 1.33x faster                                 |
| html5lib                | 86.4 ms                                                             | 65.3 ms: 1.32x faster                                 |
| unpickle_pure_python    | 300 us                                                              | 231 us: 1.30x faster                                  |
| regex_compile           | 177 ms                                                              | 137 ms: 1.29x faster                                  |
| 2to3                    | 336 ms                                                              | 264 ms: 1.27x faster                                  |
| scimark_fft             | 425 ms                                                              | 335 ms: 1.27x faster                                  |
| pycparser               | 1.53 sec                                                            | 1.24 sec: 1.24x faster                                |
| fannkuch                | 485 ms                                                              | 401 ms: 1.21x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 78.5 ms: 1.21x faster                                 |
| dulwich_log             | 76.3 ms                                                             | 63.8 ms: 1.20x faster                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                 |
| sqlite_synth            | 2.97 us                                                             | 2.51 us: 1.18x faster                                 |
| nqueens                 | 98.8 ms                                                             | 85.2 ms: 1.16x faster                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.85 ms: 1.16x faster                                 |
| sympy_sum               | 185 ms                                                              | 160 ms: 1.16x faster                                  |
| sympy_str               | 328 ms                                                              | 287 ms: 1.14x faster                                  |
| sympy_expand            | 540 ms                                                              | 476 ms: 1.13x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.5 ms: 1.10x faster                                 |
| meteor_contest          | 115 ms                                                              | 107 ms: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                  |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                 |
| pickle                  | 10.2 us                                                             | 9.55 us: 1.07x faster                                 |
| json                    | 5.41 ms                                                             | 5.07 ms: 1.07x faster                                 |
| unpickle                | 15.0 us                                                             | 14.1 us: 1.06x faster                                 |
| xml_etree_parse         | 164 ms                                                              | 157 ms: 1.04x faster                                  |
| json_loads              | 29.3 us                                                             | 28.1 us: 1.04x faster                                 |
| pickle_list             | 4.73 us                                                             | 4.57 us: 1.04x faster                                 |
| telco                   | 6.67 ms                                                             | 6.59 ms: 1.01x faster                                 |
| pickle_dict             | 27.8 us                                                             | 27.6 us: 1.00x faster                                 |
| unpickle_list           | 4.94 us                                                             | 4.97 us: 1.01x slower                                 |
| python_startup_no_site  | 5.80 ms                                                             | 5.98 ms: 1.03x slower                                 |
| regex_effbot            | 3.22 ms                                                             | 3.34 ms: 1.04x slower                                 |
| regex_v8                | 24.9 ms                                                             | 25.9 ms: 1.04x slower                                 |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                  |
| regex_dna               | 213 ms                                                              | 231 ms: 1.09x slower                                  |
| Geometric mean          | (ref)                                                               | 1.26x faster                                          |
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
