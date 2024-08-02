# Results vs. base

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 208 ms                                                                                                                 | 234 ms: 1.13x slower                                                                                                       |
| chameleon      | 4.71 ms                                                                                                                | 5.07 ms: 1.08x slower                                                                                                      |
| docutils       | 1.61 sec                                                                                                               | 1.79 sec: 1.11x slower                                                                                                     |
| html5lib       | 35.2 ms                                                                                                                | 37.0 ms: 1.05x slower                                                                                                      |
| tornado_http   | 81.6 ms                                                                                                                | 85.9 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.08x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 609 ms                                                                                                                 | 623 ms: 1.02x slower                                                                                                       |
| async_tree_cpu_io_mixed | 390 ms                                                                                                                 | 399 ms: 1.02x slower                                                                                                       |
| async_tree_none_tg      | 204 ms                                                                                                                 | 213 ms: 1.04x slower                                                                                                       |
| async_tree_none         | 216 ms                                                                                                                 | 226 ms: 1.05x slower                                                                                                       |
| async_tree_memoization  | 265 ms                                                                                                                 | 278 ms: 1.05x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 66.2 ms                                                                                                                | 51.5 ms: 1.28x faster                                                                                                      |
| float          | 48.2 ms                                                                                                                | 43.4 ms: 1.11x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.13x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                                                                 | 119 ms: 1.01x slower                                                                                                       |
| regex_effbot   | 1.57 ms                                                                                                                | 1.58 ms: 1.01x slower                                                                                                      |
| regex_compile  | 76.9 ms                                                                                                                | 88.6 ms: 1.15x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.05x slower                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| pickle_dict          | 19.4 us                                                                                                                | 17.6 us: 1.10x faster                                                                                                      |
| tomli_loads          | 1.35 sec                                                                                                               | 1.25 sec: 1.08x faster                                                                                                     |
| xml_etree_iterparse  | 61.8 ms                                                                                                                | 60.0 ms: 1.03x faster                                                                                                      |
| xml_etree_generate   | 52.9 ms                                                                                                                | 51.6 ms: 1.03x faster                                                                                                      |
| xml_etree_parse      | 91.3 ms                                                                                                                | 90.3 ms: 1.01x faster                                                                                                      |
| pickle_pure_python   | 173 us                                                                                                                 | 174 us: 1.01x slower                                                                                                       |
| json_loads           | 14.0 us                                                                                                                | 14.2 us: 1.01x slower                                                                                                      |
| xml_etree_process    | 35.9 ms                                                                                                                | 36.4 ms: 1.02x slower                                                                                                      |
| unpickle             | 8.45 us                                                                                                                | 8.60 us: 1.02x slower                                                                                                      |
| json_dumps           | 5.57 ms                                                                                                                | 5.70 ms: 1.02x slower                                                                                                      |
| pickle_list          | 2.94 us                                                                                                                | 3.05 us: 1.04x slower                                                                                                      |
| unpickle_pure_python | 120 us                                                                                                                 | 126 us: 1.05x slower                                                                                                       |
| unpickle_list        | 2.62 us                                                                                                                | 2.82 us: 1.07x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.2 ms                                                                                                                | 22.0 ms: 1.09x slower                                                                                                      |
| python_startup_no_site | 16.4 ms                                                                                                                | 18.2 ms: 1.11x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.10x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.28 ms                                                                                                                | 4.93 ms: 1.27x faster                                                                                                      |
| django_template | 21.1 ms                                                                                                                | 25.8 ms: 1.22x slower                                                                                                      |
| genshi_text     | 14.5 ms                                                                                                                | 18.7 ms: 1.29x slower                                                                                                      |
| genshi_xml      | 31.7 ms                                                                                                                | 45.6 ms: 1.44x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.16x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 60.1 ms                                                                                                                | 44.1 ms: 1.36x faster                                                                                                      |
| nbody                    | 66.2 ms                                                                                                                | 51.5 ms: 1.28x faster                                                                                                      |
| mako                     | 6.28 ms                                                                                                                | 4.93 ms: 1.27x faster                                                                                                      |
| scimark_fft              | 172 ms                                                                                                                 | 150 ms: 1.15x faster                                                                                                       |
| scimark_sparse_mat_mult  | 2.39 ms                                                                                                                | 2.10 ms: 1.14x faster                                                                                                      |
| float                    | 48.2 ms                                                                                                                | 43.4 ms: 1.11x faster                                                                                                      |
| fannkuch                 | 238 ms                                                                                                                 | 216 ms: 1.10x faster                                                                                                       |
| pickle_dict              | 19.4 us                                                                                                                | 17.6 us: 1.10x faster                                                                                                      |
| crypto_pyaes             | 44.9 ms                                                                                                                | 41.0 ms: 1.10x faster                                                                                                      |
| tomli_loads              | 1.35 sec                                                                                                               | 1.25 sec: 1.08x faster                                                                                                     |
| pyflate                  | 276 ms                                                                                                                 | 257 ms: 1.08x faster                                                                                                       |
| deepcopy_memo            | 21.7 us                                                                                                                | 20.6 us: 1.06x faster                                                                                                      |
| pprint_safe_repr         | 467 ms                                                                                                                 | 446 ms: 1.05x faster                                                                                                       |
| pprint_pformat           | 959 ms                                                                                                                 | 924 ms: 1.04x faster                                                                                                       |
| xml_etree_iterparse      | 61.8 ms                                                                                                                | 60.0 ms: 1.03x faster                                                                                                      |
| xml_etree_generate       | 52.9 ms                                                                                                                | 51.6 ms: 1.03x faster                                                                                                      |
| scimark_monte_carlo      | 39.1 ms                                                                                                                | 38.2 ms: 1.02x faster                                                                                                      |
| sqlite_synth             | 1.61 us                                                                                                                | 1.59 us: 1.01x faster                                                                                                      |
| xml_etree_parse          | 91.3 ms                                                                                                                | 90.3 ms: 1.01x faster                                                                                                      |
| telco                    | 4.59 ms                                                                                                                | 4.55 ms: 1.01x faster                                                                                                      |
| gc_traversal             | 1.56 ms                                                                                                                | 1.57 ms: 1.01x slower                                                                                                      |
| pickle_pure_python       | 173 us                                                                                                                 | 174 us: 1.01x slower                                                                                                       |
| regex_dna                | 118 ms                                                                                                                 | 119 ms: 1.01x slower                                                                                                       |
| regex_effbot             | 1.57 ms                                                                                                                | 1.58 ms: 1.01x slower                                                                                                      |
| json_loads               | 14.0 us                                                                                                                | 14.2 us: 1.01x slower                                                                                                      |
| pathlib                  | 79.3 ms                                                                                                                | 80.2 ms: 1.01x slower                                                                                                      |
| comprehensions           | 10.1 us                                                                                                                | 10.2 us: 1.02x slower                                                                                                      |
| xml_etree_process        | 35.9 ms                                                                                                                | 36.4 ms: 1.02x slower                                                                                                      |
| unpickle                 | 8.45 us                                                                                                                | 8.60 us: 1.02x slower                                                                                                      |
| create_gc_cycles         | 903 us                                                                                                                 | 920 us: 1.02x slower                                                                                                       |
| coverage                 | 43.5 ms                                                                                                                | 44.5 ms: 1.02x slower                                                                                                      |
| json_dumps               | 5.57 ms                                                                                                                | 5.70 ms: 1.02x slower                                                                                                      |
| async_tree_io_tg         | 609 ms                                                                                                                 | 623 ms: 1.02x slower                                                                                                       |
| logging_simple           | 5.73 us                                                                                                                | 5.87 us: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed  | 390 ms                                                                                                                 | 399 ms: 1.02x slower                                                                                                       |
| chaos                    | 38.2 ms                                                                                                                | 39.2 ms: 1.02x slower                                                                                                      |
| meteor_contest           | 71.0 ms                                                                                                                | 72.8 ms: 1.03x slower                                                                                                      |
| logging_format           | 6.12 us                                                                                                                | 6.29 us: 1.03x slower                                                                                                      |
| pickle_list              | 2.94 us                                                                                                                | 3.05 us: 1.04x slower                                                                                                      |
| coroutines               | 12.7 ms                                                                                                                | 13.2 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg       | 204 ms                                                                                                                 | 213 ms: 1.04x slower                                                                                                       |
| async_tree_none          | 216 ms                                                                                                                 | 226 ms: 1.05x slower                                                                                                       |
| async_tree_memoization   | 265 ms                                                                                                                 | 278 ms: 1.05x slower                                                                                                       |
| unpickle_pure_python     | 120 us                                                                                                                 | 126 us: 1.05x slower                                                                                                       |
| html5lib                 | 35.2 ms                                                                                                                | 37.0 ms: 1.05x slower                                                                                                      |
| aiohttp                  | 894 us                                                                                                                 | 940 us: 1.05x slower                                                                                                       |
| tornado_http             | 81.6 ms                                                                                                                | 85.9 ms: 1.05x slower                                                                                                      |
| logging_silent           | 52.8 ns                                                                                                                | 55.9 ns: 1.06x slower                                                                                                      |
| sqlglot_parse            | 749 us                                                                                                                 | 800 us: 1.07x slower                                                                                                       |
| unpickle_list            | 2.62 us                                                                                                                | 2.82 us: 1.07x slower                                                                                                      |
| dulwich_log              | 39.1 ms                                                                                                                | 42.1 ms: 1.08x slower                                                                                                      |
| chameleon                | 4.71 ms                                                                                                                | 5.07 ms: 1.08x slower                                                                                                      |
| sqlglot_transpile        | 954 us                                                                                                                 | 1.03 ms: 1.08x slower                                                                                                      |
| deepcopy_reduce          | 1.97 us                                                                                                                | 2.14 us: 1.08x slower                                                                                                      |
| pycparser                | 697 ms                                                                                                                 | 756 ms: 1.08x slower                                                                                                       |
| deepcopy                 | 218 us                                                                                                                 | 238 us: 1.09x slower                                                                                                       |
| raytrace                 | 161 ms                                                                                                                 | 175 ms: 1.09x slower                                                                                                       |
| python_startup           | 20.2 ms                                                                                                                | 22.0 ms: 1.09x slower                                                                                                      |
| async_generators         | 226 ms                                                                                                                 | 248 ms: 1.09x slower                                                                                                       |
| mdp                      | 1.33 sec                                                                                                               | 1.46 sec: 1.09x slower                                                                                                     |
| nqueens                  | 55.5 ms                                                                                                                | 61.4 ms: 1.11x slower                                                                                                      |
| docutils                 | 1.61 sec                                                                                                               | 1.79 sec: 1.11x slower                                                                                                     |
| sympy_sum                | 83.8 ms                                                                                                                | 93.1 ms: 1.11x slower                                                                                                      |
| python_startup_no_site   | 16.4 ms                                                                                                                | 18.2 ms: 1.11x slower                                                                                                      |
| generators               | 19.3 ms                                                                                                                | 21.6 ms: 1.12x slower                                                                                                      |
| bench_mp_pool            | 66.2 ms                                                                                                                | 73.9 ms: 1.12x slower                                                                                                      |
| go                       | 83.5 ms                                                                                                                | 93.6 ms: 1.12x slower                                                                                                      |
| typing_runtime_protocols | 100 us                                                                                                                 | 112 us: 1.12x slower                                                                                                       |
| scimark_sor              | 73.1 ms                                                                                                                | 82.2 ms: 1.12x slower                                                                                                      |
| richards_super           | 29.3 ms                                                                                                                | 33.0 ms: 1.13x slower                                                                                                      |
| sqlglot_optimize         | 32.6 ms                                                                                                                | 36.7 ms: 1.13x slower                                                                                                      |
| 2to3                     | 208 ms                                                                                                                 | 234 ms: 1.13x slower                                                                                                       |
| richards                 | 25.8 ms                                                                                                                | 29.1 ms: 1.13x slower                                                                                                      |
| sympy_str                | 158 ms                                                                                                                 | 179 ms: 1.14x slower                                                                                                       |
| thrift                   | 8.07 ms                                                                                                                | 9.28 ms: 1.15x slower                                                                                                      |
| regex_compile            | 76.9 ms                                                                                                                | 88.6 ms: 1.15x slower                                                                                                      |
| sympy_integrate          | 12.1 ms                                                                                                                | 14.0 ms: 1.16x slower                                                                                                      |
| pylint                   | 206 ms                                                                                                                 | 238 ms: 1.16x slower                                                                                                       |
| sympy_expand             | 267 ms                                                                                                                 | 311 ms: 1.16x slower                                                                                                       |
| bench_thread_pool        | 808 us                                                                                                                 | 944 us: 1.17x slower                                                                                                       |
| mypy2                    | 417 ms                                                                                                                 | 488 ms: 1.17x slower                                                                                                       |
| django_template          | 21.1 ms                                                                                                                | 25.8 ms: 1.22x slower                                                                                                      |
| deltablue                | 1.90 ms                                                                                                                | 2.37 ms: 1.25x slower                                                                                                      |
| hexiom                   | 3.64 ms                                                                                                                | 4.67 ms: 1.28x slower                                                                                                      |
| genshi_text              | 14.5 ms                                                                                                                | 18.7 ms: 1.29x slower                                                                                                      |
| scimark_lu               | 53.7 ms                                                                                                                | 72.2 ms: 1.34x slower                                                                                                      |
| genshi_xml               | 31.7 ms                                                                                                                | 45.6 ms: 1.44x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

Benchmark hidden because not significant (10): json, flaskblogging, pickle, pidigits, asyncio_tcp, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_io, async_tree_memoization_tg, regex_v8
Ignored benchmarks (1) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown