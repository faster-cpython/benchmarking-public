# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                                               | 294 ms: 1.08x slower                                                                                       |
| chameleon      | 6.93 ms                                                                                              | 7.76 ms: 1.12x slower                                                                                      |
| docutils       | 2.69 sec                                                                                             | 2.89 sec: 1.07x slower                                                                                     |
| html5lib       | 66.3 ms                                                                                              | 71.7 ms: 1.08x slower                                                                                      |
| tornado_http   | 97.6 ms                                                                                              | 108 ms: 1.10x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.09x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 733 ms                                                                                               | 804 ms: 1.10x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 760 ms                                                                                               | 850 ms: 1.12x slower                                                                                       |
| async_tree_memoization_tg  | 618 ms                                                                                               | 692 ms: 1.12x slower                                                                                       |
| async_tree_memoization     | 583 ms                                                                                               | 657 ms: 1.13x slower                                                                                       |
| async_tree_none            | 451 ms                                                                                               | 509 ms: 1.13x slower                                                                                       |
| async_tree_io              | 1.22 sec                                                                                             | 1.39 sec: 1.14x slower                                                                                     |
| async_tree_none_tg         | 471 ms                                                                                               | 540 ms: 1.15x slower                                                                                       |
| async_tree_io_tg           | 1.26 sec                                                                                             | 1.45 sec: 1.15x slower                                                                                     |
| Geometric mean             | (ref)                                                                                                | 1.13x slower                                                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                                               | 194 ms: 1.02x faster                                                                                       |
| float          | 83.5 ms                                                                                              | 95.5 ms: 1.14x slower                                                                                      |
| nbody          | 91.0 ms                                                                                              | 110 ms: 1.20x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.10x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                                               | 222 ms: 1.01x slower                                                                                       |
| regex_v8       | 25.0 ms                                                                                              | 25.9 ms: 1.04x slower                                                                                      |
| regex_effbot   | 3.57 ms                                                                                              | 3.83 ms: 1.07x slower                                                                                      |
| regex_compile  | 137 ms                                                                                               | 149 ms: 1.09x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.05x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pickle_list          | 5.07 us                                                                                              | 4.71 us: 1.08x faster                                                                                      |
| pickle_dict          | 34.9 us                                                                                              | 32.7 us: 1.06x faster                                                                                      |
| pickle               | 11.8 us                                                                                              | 11.4 us: 1.04x faster                                                                                      |
| unpickle             | 15.7 us                                                                                              | 15.4 us: 1.02x faster                                                                                      |
| unpickle_list        | 5.12 us                                                                                              | 5.26 us: 1.03x slower                                                                                      |
| xml_etree_iterparse  | 108 ms                                                                                               | 114 ms: 1.06x slower                                                                                       |
| json_dumps           | 10.7 ms                                                                                              | 11.3 ms: 1.06x slower                                                                                      |
| tomli_loads          | 2.23 sec                                                                                             | 2.37 sec: 1.06x slower                                                                                     |
| pickle_pure_python   | 313 us                                                                                               | 335 us: 1.07x slower                                                                                       |
| json_loads           | 28.7 us                                                                                              | 30.9 us: 1.08x slower                                                                                      |
| unpickle_pure_python | 224 us                                                                                               | 246 us: 1.10x slower                                                                                       |
| xml_etree_parse      | 162 ms                                                                                               | 472 ms: 2.91x slower                                                                                       |
| xml_etree_process    | 60.5 ms                                                                                              | 1.03 sec: 17.00x slower                                                                                    |
| xml_etree_generate   | 88.2 ms                                                                                              | 1.58 sec: 17.92x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                | 1.65x slower                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.26 ms                                                                                              | 9.60 ms: 1.04x slower                                                                                      |
| python_startup         | 10.7 ms                                                                                              | 11.1 ms: 1.04x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                | 1.04x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| genshi_text     | 23.8 ms                                                                                              | 24.9 ms: 1.04x slower                                                                                      |
| genshi_xml      | 52.1 ms                                                                                              | 56.2 ms: 1.08x slower                                                                                      |
| django_template | 35.2 ms                                                                                              | 38.3 ms: 1.09x slower                                                                                      |
| mako            | 11.7 ms                                                                                              | 12.9 ms: 1.11x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                | 1.08x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 1.48 ms                                                                                              | 1.22 ms: 1.22x faster                                                                                      |
| gc_traversal               | 4.37 ms                                                                                              | 3.64 ms: 1.20x faster                                                                                      |
| pickle_list                | 5.07 us                                                                                              | 4.71 us: 1.08x faster                                                                                      |
| pickle_dict                | 34.9 us                                                                                              | 32.7 us: 1.06x faster                                                                                      |
| bench_mp_pool              | 23.9 ms                                                                                              | 22.6 ms: 1.06x faster                                                                                      |
| pickle                     | 11.8 us                                                                                              | 11.4 us: 1.04x faster                                                                                      |
| unpickle                   | 15.7 us                                                                                              | 15.4 us: 1.02x faster                                                                                      |
| pidigits                   | 197 ms                                                                                               | 194 ms: 1.02x faster                                                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                                                             | 1.85 sec: 1.01x slower                                                                                     |
| regex_dna                  | 219 ms                                                                                               | 222 ms: 1.01x slower                                                                                       |
| asyncio_tcp                | 501 ms                                                                                               | 511 ms: 1.02x slower                                                                                       |
| unpickle_list              | 5.12 us                                                                                              | 5.26 us: 1.03x slower                                                                                      |
| regex_v8                   | 25.0 ms                                                                                              | 25.9 ms: 1.04x slower                                                                                      |
| python_startup_no_site     | 9.26 ms                                                                                              | 9.60 ms: 1.04x slower                                                                                      |
| generators                 | 30.1 ms                                                                                              | 31.2 ms: 1.04x slower                                                                                      |
| genshi_text                | 23.8 ms                                                                                              | 24.9 ms: 1.04x slower                                                                                      |
| python_startup             | 10.7 ms                                                                                              | 11.1 ms: 1.04x slower                                                                                      |
| richards                   | 49.7 ms                                                                                              | 51.9 ms: 1.04x slower                                                                                      |
| dulwich_log                | 67.6 ms                                                                                              | 70.8 ms: 1.05x slower                                                                                      |
| pyflate                    | 484 ms                                                                                               | 510 ms: 1.05x slower                                                                                       |
| xml_etree_iterparse        | 108 ms                                                                                               | 114 ms: 1.06x slower                                                                                       |
| json_dumps                 | 10.7 ms                                                                                              | 11.3 ms: 1.06x slower                                                                                      |
| meteor_contest             | 110 ms                                                                                               | 117 ms: 1.06x slower                                                                                       |
| nqueens                    | 83.5 ms                                                                                              | 88.6 ms: 1.06x slower                                                                                      |
| gunicorn                   | 1.27 ms                                                                                              | 1.35 ms: 1.06x slower                                                                                      |
| go                         | 148 ms                                                                                               | 157 ms: 1.06x slower                                                                                       |
| tomli_loads                | 2.23 sec                                                                                             | 2.37 sec: 1.06x slower                                                                                     |
| pathlib                    | 18.6 ms                                                                                              | 19.8 ms: 1.06x slower                                                                                      |
| logging_silent             | 109 ns                                                                                               | 116 ns: 1.07x slower                                                                                       |
| typing_runtime_protocols   | 119 us                                                                                               | 127 us: 1.07x slower                                                                                       |
| aiohttp                    | 1.17 ms                                                                                              | 1.25 ms: 1.07x slower                                                                                      |
| pycparser                  | 1.19 sec                                                                                             | 1.27 sec: 1.07x slower                                                                                     |
| pickle_pure_python         | 313 us                                                                                               | 335 us: 1.07x slower                                                                                       |
| regex_effbot               | 3.57 ms                                                                                              | 3.83 ms: 1.07x slower                                                                                      |
| richards_super             | 55.1 ms                                                                                              | 59.1 ms: 1.07x slower                                                                                      |
| docutils                   | 2.69 sec                                                                                             | 2.89 sec: 1.07x slower                                                                                     |
| genshi_xml                 | 52.1 ms                                                                                              | 56.2 ms: 1.08x slower                                                                                      |
| pprint_safe_repr           | 753 ms                                                                                               | 812 ms: 1.08x slower                                                                                       |
| json_loads                 | 28.7 us                                                                                              | 30.9 us: 1.08x slower                                                                                      |
| deepcopy_memo              | 39.8 us                                                                                              | 43.0 us: 1.08x slower                                                                                      |
| html5lib                   | 66.3 ms                                                                                              | 71.7 ms: 1.08x slower                                                                                      |
| scimark_fft                | 375 ms                                                                                               | 405 ms: 1.08x slower                                                                                       |
| 2to3                       | 272 ms                                                                                               | 294 ms: 1.08x slower                                                                                       |
| pprint_pformat             | 1.54 sec                                                                                             | 1.66 sec: 1.08x slower                                                                                     |
| comprehensions             | 17.0 us                                                                                              | 18.5 us: 1.08x slower                                                                                      |
| chaos                      | 63.4 ms                                                                                              | 68.7 ms: 1.08x slower                                                                                      |
| json                       | 5.24 ms                                                                                              | 5.68 ms: 1.08x slower                                                                                      |
| scimark_lu                 | 117 ms                                                                                               | 126 ms: 1.08x slower                                                                                       |
| hexiom                     | 6.32 ms                                                                                              | 6.86 ms: 1.09x slower                                                                                      |
| django_template            | 35.2 ms                                                                                              | 38.3 ms: 1.09x slower                                                                                      |
| scimark_monte_carlo        | 70.0 ms                                                                                              | 76.1 ms: 1.09x slower                                                                                      |
| async_generators           | 459 ms                                                                                               | 500 ms: 1.09x slower                                                                                       |
| regex_compile              | 137 ms                                                                                               | 149 ms: 1.09x slower                                                                                       |
| pylint                     | 313 ms                                                                                               | 341 ms: 1.09x slower                                                                                       |
| logging_format             | 6.50 us                                                                                              | 7.09 us: 1.09x slower                                                                                      |
| scimark_sparse_mat_mult    | 5.13 ms                                                                                              | 5.61 ms: 1.09x slower                                                                                      |
| crypto_pyaes               | 73.3 ms                                                                                              | 80.1 ms: 1.09x slower                                                                                      |
| logging_simple             | 5.89 us                                                                                              | 6.44 us: 1.09x slower                                                                                      |
| mdp                        | 2.64 sec                                                                                             | 2.89 sec: 1.09x slower                                                                                     |
| sqlglot_optimize           | 54.3 ms                                                                                              | 59.4 ms: 1.09x slower                                                                                      |
| sqlglot_transpile          | 1.64 ms                                                                                              | 1.79 ms: 1.09x slower                                                                                      |
| sqlglot_parse              | 1.31 ms                                                                                              | 1.44 ms: 1.09x slower                                                                                      |
| async_tree_cpu_io_mixed    | 733 ms                                                                                               | 804 ms: 1.10x slower                                                                                       |
| unpickle_pure_python       | 224 us                                                                                               | 246 us: 1.10x slower                                                                                       |
| sqlglot_normalize          | 107 ms                                                                                               | 118 ms: 1.10x slower                                                                                       |
| raytrace                   | 284 ms                                                                                               | 314 ms: 1.10x slower                                                                                       |
| tornado_http               | 97.6 ms                                                                                              | 108 ms: 1.10x slower                                                                                       |
| scimark_sor                | 126 ms                                                                                               | 140 ms: 1.11x slower                                                                                       |
| deepcopy                   | 354 us                                                                                               | 392 us: 1.11x slower                                                                                       |
| mako                       | 11.7 ms                                                                                              | 12.9 ms: 1.11x slower                                                                                      |
| async_tree_cpu_io_mixed_tg | 760 ms                                                                                               | 850 ms: 1.12x slower                                                                                       |
| chameleon                  | 6.93 ms                                                                                              | 7.76 ms: 1.12x slower                                                                                      |
| async_tree_memoization_tg  | 618 ms                                                                                               | 692 ms: 1.12x slower                                                                                       |
| fannkuch                   | 402 ms                                                                                               | 451 ms: 1.12x slower                                                                                       |
| deepcopy_reduce            | 3.14 us                                                                                              | 3.53 us: 1.12x slower                                                                                      |
| sqlite_synth               | 2.87 us                                                                                              | 3.23 us: 1.12x slower                                                                                      |
| telco                      | 8.53 ms                                                                                              | 9.60 ms: 1.13x slower                                                                                      |
| async_tree_memoization     | 583 ms                                                                                               | 657 ms: 1.13x slower                                                                                       |
| async_tree_none            | 451 ms                                                                                               | 509 ms: 1.13x slower                                                                                       |
| async_tree_io              | 1.22 sec                                                                                             | 1.39 sec: 1.14x slower                                                                                     |
| coroutines                 | 21.8 ms                                                                                              | 24.8 ms: 1.14x slower                                                                                      |
| float                      | 83.5 ms                                                                                              | 95.5 ms: 1.14x slower                                                                                      |
| sympy_integrate            | 20.0 ms                                                                                              | 22.9 ms: 1.15x slower                                                                                      |
| async_tree_none_tg         | 471 ms                                                                                               | 540 ms: 1.15x slower                                                                                       |
| async_tree_io_tg           | 1.26 sec                                                                                             | 1.45 sec: 1.15x slower                                                                                     |
| deltablue                  | 3.44 ms                                                                                              | 3.99 ms: 1.16x slower                                                                                      |
| spectral_norm              | 111 ms                                                                                               | 130 ms: 1.17x slower                                                                                       |
| flaskblogging              | 8.70 ms                                                                                              | 10.2 ms: 1.17x slower                                                                                      |
| nbody                      | 91.0 ms                                                                                              | 110 ms: 1.20x slower                                                                                       |
| sympy_str                  | 273 ms                                                                                               | 332 ms: 1.22x slower                                                                                       |
| bench_thread_pool          | 852 us                                                                                               | 1.09 ms: 1.27x slower                                                                                      |
| mypy2                      | 866 ms                                                                                               | 1.15 sec: 1.33x slower                                                                                     |
| sympy_expand               | 459 ms                                                                                               | 613 ms: 1.33x slower                                                                                       |
| sympy_sum                  | 151 ms                                                                                               | 211 ms: 1.39x slower                                                                                       |
| xml_etree_parse            | 162 ms                                                                                               | 472 ms: 2.91x slower                                                                                       |
| coverage                   | 95.2 ms                                                                                              | 725 ms: 7.62x slower                                                                                       |
| thrift                     | 805 us                                                                                               | 9.50 ms: 11.80x slower                                                                                     |
| xml_etree_process          | 60.5 ms                                                                                              | 1.03 sec: 17.00x slower                                                                                    |
| xml_etree_generate         | 88.2 ms                                                                                              | 1.58 sec: 17.92x slower                                                                                    |
| Geometric mean             | (ref)                                                                                                | 1.21x slower                                                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.61x