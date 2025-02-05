# Results vs. 3.12.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-x86_64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.018x faster
- HPT reliability: 76.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 312 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 325 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 313 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 394 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                       |
| float          | 76.6 ms                                                      | 73.6 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.63 us: 1.01x faster                                                       |
| unpickle             | 14.8 us                                                      | 14.9 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.54 us: 1.02x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 325 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 313 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 394 ms: 1.37x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.9 us: 1.37x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 298 us: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.9 ms: 1.15x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody                      | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.01 ms: 1.05x faster                                                       |
| scimark_fft                | 301 ms                                                       | 287 ms: 1.05x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.66 us: 1.04x faster                                                       |
| float                      | 76.6 ms                                                      | 73.6 ms: 1.04x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.26 us: 1.03x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.6 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 927 us: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.17 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| go                         | 150 ms                                                       | 148 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 387 ms: 1.01x faster                                                        |
| json_loads                 | 24.4 us                                                      | 24.2 us: 1.01x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.5 ms: 1.01x faster                                                       |
| unpickle_list              | 4.66 us                                                      | 4.63 us: 1.01x faster                                                       |
| generators                 | 37.4 ms                                                      | 37.3 ms: 1.00x faster                                                       |
| unpickle                   | 14.8 us                                                      | 14.9 us: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.6 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| pyflate                    | 439 ms                                                       | 445 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.54 us: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                        |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| sympy_str                  | 302 ms                                                       | 313 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 170 ms: 1.05x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.9 ms: 1.05x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                      |
| bench_mp_pool              | 4.76 ms                                                      | 5.08 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                       |
| 2to3                       | 285 ms                                                       | 312 ms: 1.09x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 98.2 ms: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.10x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.5 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                      |
| sympy_expand               | 484 ms                                                       | 537 ms: 1.11x slower                                                        |
| django_template            | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| raytrace                   | 298 ms                                                       | 332 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 65.6 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.95 ms: 1.17x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.20 ms: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.20x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.42 ms: 1.27x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 87.7 ns: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (6): logging_simple, scimark_lu, xml_etree_parse, asyncio_tcp_ssl, pprint_pformat, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 76.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x