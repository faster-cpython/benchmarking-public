
# Results vs. 3.10.4

- fork: python
- ref: 3c67ec394faac79d2608
- machine: darwin-arm64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| html5lib       | 44.2 ms                                                | 34.8 ms: 1.27x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 52.1 ms: 1.39x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.3 ms: 1.33x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.47x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.10 ms: 1.38x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 157 us: 1.30x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 34.6 ms: 1.29x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.4 ms: 1.10x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.76 us: 1.02x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                                 |
| pickle               | 7.35 us                                                | 7.47 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.19 ms: 1.46x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 28.2 ms: 1.32x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.2 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.57 ms: 2.00x faster                                                 |
| logging_silent          | 119 ns                                                 | 65.8 ns: 1.81x faster                                                 |
| richards                | 51.4 ms                                                | 29.8 ms: 1.73x faster                                                 |
| scimark_lu              | 109 ms                                                 | 70.9 ms: 1.54x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 436 ms: 1.54x faster                                                  |
| go                      | 165 ms                                                 | 110 ms: 1.51x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 327 ms: 1.50x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.8 ms: 1.48x faster                                                 |
| scimark_sor             | 126 ms                                                 | 85.3 ms: 1.48x faster                                                 |
| raytrace                | 325 ms                                                 | 221 ms: 1.47x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.47x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.32 ms: 1.46x faster                                                 |
| chaos                   | 66.7 ms                                                | 45.7 ms: 1.46x faster                                                 |
| mako                    | 10.5 ms                                                | 7.19 ms: 1.46x faster                                                 |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 50.0 ms: 1.45x faster                                                 |
| async_tree_none         | 400 ms                                                 | 284 ms: 1.41x faster                                                  |
| float                   | 72.4 ms                                                | 52.1 ms: 1.39x faster                                                 |
| pycparser               | 916 ms                                                 | 664 ms: 1.38x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.10 ms: 1.38x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 742 ms: 1.37x faster                                                  |
| pyflate                 | 453 ms                                                 | 331 ms: 1.37x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.02 ms: 1.34x faster                                                 |
| regex_compile           | 96.4 ms                                                | 72.3 ms: 1.33x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.33x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.19 ms: 1.32x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.5 ms: 1.32x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 28.2 ms: 1.32x faster                                                 |
| thrift                  | 580 us                                                 | 442 us: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 157 us: 1.30x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.6 ms: 1.29x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.2 ms: 1.29x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 469 ms: 1.29x faster                                                  |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 963 ms: 1.28x faster                                                  |
| deepcopy                | 281 us                                                 | 220 us: 1.28x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.64 us: 1.27x faster                                                 |
| logging_format          | 4.97 us                                                | 3.91 us: 1.27x faster                                                 |
| html5lib                | 44.2 ms                                                | 34.8 ms: 1.27x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.01 ms: 1.27x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 695 us: 1.27x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.4 ms: 1.26x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 538 ms: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 256 ms: 1.24x faster                                                  |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.80 ms: 1.23x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 1.93 us: 1.23x faster                                                 |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                 |
| scimark_fft             | 230 ms                                                 | 192 ms: 1.20x faster                                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.9 ms: 1.19x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.19x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 463 us: 1.18x faster                                                  |
| mypy2                   | 307 ms                                                 | 260 ms: 1.18x faster                                                  |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                  |
| comprehensions          | 17.6 us                                                | 15.1 us: 1.17x faster                                                 |
| sympy_str               | 169 ms                                                 | 146 ms: 1.16x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 82.1 ms: 1.14x faster                                                 |
| sympy_expand            | 275 ms                                                 | 244 ms: 1.13x faster                                                  |
| nqueens                 | 68.2 ms                                                | 60.6 ms: 1.13x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                 |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.4 ms: 1.10x faster                                                 |
| json                    | 3.08 ms                                                | 2.79 ms: 1.10x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                                 |
| telco                   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 75.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.76 us: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.47 us: 1.02x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                 |
| generators              | 32.7 ms                                                | 34.3 ms: 1.05x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.62 ms: 1.06x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.6 ms: 1.12x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                 |
| dask                    | 265 ms                                                 | 323 ms: 1.22x slower                                                  |
| coverage                | 42.0 ms                                                | 56.8 ms: 1.35x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (2): unpickle, unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
